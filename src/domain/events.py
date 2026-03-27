"""[Eorder_model_money~03] 도메인 이벤트."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class OrderCreated:
    """[Eorder_model_money] 주문 생성됨. order_constraint_order_creation_publishes_order_created."""

    order_id: str
    customer_id: str
    sku_list: list[str]
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass(frozen=True)
class OrderCancelled:
    """[Eorder_model_order_line] 주문 취소됨. order_constraint_order_cancellation_releases_allocations 트리거."""

    order_id: str
    reason: str
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass(frozen=True)
class OutOfStock:
    """[order_event_out_of_stock] 재고 부족."""

    sku: str
    requested_quantity: int
    timestamp: datetime = field(default_factory=datetime.now)
