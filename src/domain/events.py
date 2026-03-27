"""[ORD_EV_ORDER_CREATED, ORD_EV_ORDER_CANCELLED, ORD_EV_OUT_OF_STOCK] 도메인 이벤트."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class OrderCreated:
    """[ORD_EV_ORDER_CREATED] 주문 생성됨. ORD_POL_ORDER_CREATE_EMITS_ORDER_CREATED."""

    order_id: str
    customer_id: str
    sku_list: list[str]
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass(frozen=True)
class OrderCancelled:
    """[ORD_EV_ORDER_CANCELLED] 주문 취소됨. ORD_POL_ORDER_CANCEL_RELEASES_ALLOC 트리거."""

    order_id: str
    reason: str
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass(frozen=True)
class OutOfStock:
    """[ORD_EV_OUT_OF_STOCK] 재고 부족."""

    sku: str
    requested_quantity: int
    timestamp: datetime = field(default_factory=datetime.now)
