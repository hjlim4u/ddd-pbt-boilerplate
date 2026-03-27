"""도메인 모델: Value Objects (Pydantic frozen) + Entities (dataclass)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from src.domain.exceptions import (
    CannotAllocateError,
    CurrencyMismatchError,
    InvalidOrderError,
)

# ──────────────────────────────────────────────
# Value Objects (immutable)
# ──────────────────────────────────────────────


class Money(BaseModel):
    """[V-01] 금액 + 통화. INV-03: amount >= 0, FMT-01: ISO 4217."""

    model_config = ConfigDict(frozen=True)

    amount: Decimal = Field(ge=0, decimal_places=2)
    currency: str = Field(min_length=3, max_length=3, pattern=r"^[A-Z]{3}$")

    def __add__(self, other: Money) -> Money:
        """INV-03: 덧셈 후에도 amount >= 0 보장 (두 양수의 합)."""
        if self.currency != other.currency:
            raise CurrencyMismatchError(self.currency, other.currency)
        return Money(amount=self.amount + other.amount, currency=self.currency)

    def __sub__(self, other: Money) -> Money:
        """INV-03: 뺄셈 결과가 음수이면 ValueError."""
        if self.currency != other.currency:
            raise CurrencyMismatchError(self.currency, other.currency)
        result = self.amount - other.amount
        if result < 0:
            raise ValueError(f"Result would be negative: {result}")
        return Money(amount=result, currency=self.currency)


class OrderLine(BaseModel):
    """[V-02] 주문 항목. FMT-02: SKU 형식."""

    model_config = ConfigDict(frozen=True)

    order_id: str
    sku: str = Field(min_length=1, max_length=20, pattern=r"^[A-Z0-9\-]+$")
    quantity: int = Field(gt=0)

    def __hash__(self) -> int:
        return hash((self.order_id, self.sku))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, OrderLine):
            return NotImplemented
        return self.order_id == other.order_id and self.sku == other.sku


# ──────────────────────────────────────────────
# Entities
# ──────────────────────────────────────────────


@dataclass
class Order:
    """[E-01] 주문. INV-02: 최소 1개 OrderLine 필수."""

    id: str
    customer_id: str
    order_lines: list[OrderLine]
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        """INV-02: Order는 최소 1개의 OrderLine을 가져야 한다."""
        if not self.order_lines:
            raise InvalidOrderError("Order must have at least one OrderLine")


@dataclass(eq=False)
class Batch:
    """[E-02] 입고 배치. INV-01: 가용 수량 비음수."""

    reference: str
    sku: str
    purchased_quantity: int
    eta: date | None
    _allocations: set[OrderLine] = field(default_factory=set, repr=False)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Batch):
            return NotImplemented
        return self.reference == other.reference

    def __hash__(self) -> int:
        return hash(self.reference)

    @property
    def available_quantity(self) -> int:
        """INV-01: 항상 >= 0."""
        return self.purchased_quantity - sum(
            line.quantity for line in self._allocations
        )

    def can_allocate(self, line: OrderLine) -> bool:
        """POL-02: SKU 일치 + 수량 충분."""
        return self.sku == line.sku and self.available_quantity >= line.quantity

    def allocate(self, line: OrderLine) -> None:
        """INV-01: 가용 수량 비음수 보장. INV-04: 멱등성."""
        if not self.can_allocate(line):
            raise CannotAllocateError(
                line.sku,
                "SKU mismatch" if self.sku != line.sku else "insufficient quantity",
            )
        self._allocations.add(line)

    def deallocate(self, line: OrderLine) -> None:
        """배정 해제. 배정되지 않은 라인은 무시 (멱등)."""
        self._allocations.discard(line)
