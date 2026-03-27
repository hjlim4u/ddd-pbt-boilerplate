"""[EV-01~03] 도메인 이벤트."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class OrderCreated:
    """[EV-01] 주문 생성됨. POL-01."""

    order_id: str
    customer_id: str
    sku_list: list[str]
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass(frozen=True)
class OrderCancelled:
    """[EV-02] 주문 취소됨. POL-03 트리거."""

    order_id: str
    reason: str
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass(frozen=True)
class OutOfStock:
    """[EV-03] 재고 부족."""

    sku: str
    requested_quantity: int
    timestamp: datetime = field(default_factory=datetime.now)
