"""@order scope events."""

from src.catalog.types import DomainEvent


ORDER_EVENT_ORDER_CREATED = DomainEvent(
    id="ORDER_EVENT_ORDER_CREATED",
    name="OrderCreated",
    scope="@order",
    payload=("order_id", "customer_id", "order_lines[]", "timestamp"),
    trigger="고객이 결제 완료 시",
    subsequent="재고 배정 시작",
)

ORDER_EVENT_ORDER_CANCELLED = DomainEvent(
    id="ORDER_EVENT_ORDER_CANCELLED",
    name="OrderCancelled",
    scope="@order",
    payload=("order_id", "reason", "timestamp"),
    trigger="고객 취소 또는 결제 실패",
    subsequent="배정된 재고 해제",
)

ORDER_EVENT_OUT_OF_STOCK = DomainEvent(
    id="ORDER_EVENT_OUT_OF_STOCK",
    name="OutOfStock",
    scope="@order",
    payload=("sku", "requested_quantity", "timestamp"),
    trigger="배정 시 가용 수량 부족",
    subsequent="주문자에게 알림",
)

EVENTS: tuple[DomainEvent, ...] = (
    ORDER_EVENT_ORDER_CREATED,
    ORDER_EVENT_ORDER_CANCELLED,
    ORDER_EVENT_OUT_OF_STOCK,
)

__all__ = [
    "EVENTS",
    "ORDER_EVENT_ORDER_CANCELLED",
    "ORDER_EVENT_ORDER_CREATED",
    "ORDER_EVENT_OUT_OF_STOCK",
]