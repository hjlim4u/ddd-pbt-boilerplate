"""@order scope models."""

from src.catalog.types import DomainModel, ModelField

from .constraints import (
    ORDER_CONSTRAINT_ALLOCATION_REQUIRES_MATCHING_SKU,
    ORDER_CONSTRAINT_BATCH_ALLOCATION_IDEMPOTENT,
    ORDER_CONSTRAINT_BATCH_AVAILABLE_QUANTITY_NON_NEGATIVE,
    ORDER_CONSTRAINT_CURRENCY_IS_ISO_4217_UPPERCASE,
    ORDER_CONSTRAINT_MONEY_AMOUNT_NON_NEGATIVE,
    ORDER_CONSTRAINT_ORDER_CANCELLATION_RELEASES_ALLOCATIONS,
    ORDER_CONSTRAINT_ORDER_CREATION_PUBLISHES_ORDER_CREATED,
    ORDER_CONSTRAINT_ORDER_REQUIRES_AT_LEAST_ONE_ORDER_LINE,
    ORDER_CONSTRAINT_SKU_IS_UPPERCASE_ALNUM_HYPHEN_MAX_20,
)
from .events import ORDER_EVENT_ORDER_CANCELLED, ORDER_EVENT_ORDER_CREATED, ORDER_EVENT_OUT_OF_STOCK
from .properties import (
    ORDER_PROPERTY_ALLOCATION_REQUIRES_MATCHING_SKU,
    ORDER_PROPERTY_BATCH_ALLOCATION_IDEMPOTENT,
    ORDER_PROPERTY_BATCH_AVAILABLE_QUANTITY_NON_NEGATIVE,
    ORDER_PROPERTY_MONEY_ADDITION_IS_COMMUTATIVE,
    ORDER_PROPERTY_MONEY_SERIALIZATION_ROUND_TRIP,
    ORDER_PROPERTY_ORDER_LINE_SKU_FORMAT_VALIDATION,
    ORDER_PROPERTY_ORDER_REQUIRES_AT_LEAST_ONE_ORDER_LINE,
)


ORDER_MODEL_MONEY = DomainModel(
    id="ORDER_MODEL_MONEY",
    name="Money",
    model_type="ValueObject",
    scope="@order",
    fields=(
        ModelField("ORDER_MODEL_MONEY_FIELD_AMOUNT", "amount", "Decimal", ">= 0, 소수점 2자리"),
        ModelField("ORDER_MODEL_MONEY_FIELD_CURRENCY", "currency", "str", "ISO 4217 3자리"),
    ),
    doc_file="docs/order/money.md",
    constraints=(ORDER_CONSTRAINT_MONEY_AMOUNT_NON_NEGATIVE, ORDER_CONSTRAINT_CURRENCY_IS_ISO_4217_UPPERCASE),
    properties=(ORDER_PROPERTY_MONEY_SERIALIZATION_ROUND_TRIP, ORDER_PROPERTY_MONEY_ADDITION_IS_COMMUTATIVE),
)

ORDER_MODEL_ORDER_LINE = DomainModel(
    id="ORDER_MODEL_ORDER_LINE",
    name="OrderLine",
    model_type="ValueObject",
    scope="@order",
    fields=(
        ModelField("ORDER_MODEL_ORDER_LINE_FIELD_ORDER_ID", "order_id", "str", ""),
        ModelField("ORDER_MODEL_ORDER_LINE_FIELD_SKU", "sku", "str", "대문자 영숫자+하이픈, 최대 20자"),
        ModelField("ORDER_MODEL_ORDER_LINE_FIELD_QUANTITY", "quantity", "int", "> 0"),
    ),
    doc_file="docs/order/orderline.md",
    constraints=(ORDER_CONSTRAINT_SKU_IS_UPPERCASE_ALNUM_HYPHEN_MAX_20,),
    properties=(ORDER_PROPERTY_ORDER_LINE_SKU_FORMAT_VALIDATION,),
)

ORDER_MODEL_ORDER = DomainModel(
    id="ORDER_MODEL_ORDER",
    name="Order",
    model_type="Entity",
    scope="@order",
    fields=(
        ModelField("ORDER_MODEL_ORDER_FIELD_ID", "id", "str", "UUID"),
        ModelField("ORDER_MODEL_ORDER_FIELD_CUSTOMER_ID", "customer_id", "str", ""),
        ModelField("ORDER_MODEL_ORDER_FIELD_ORDER_LINES", "order_lines", "list[OrderLine]", "최소 1개"),
        ModelField("ORDER_MODEL_ORDER_FIELD_CREATED_AT", "created_at", "datetime", ""),
        ModelField(
            "ORDER_MODEL_ORDER_FIELD_PENDING_EVENTS",
            "pending_events",
            "list[OrderCreated | OrderCancelled]",
            "",
        ),
    ),
    doc_file="docs/order/order.md",
    constraints=(
        ORDER_CONSTRAINT_ORDER_REQUIRES_AT_LEAST_ONE_ORDER_LINE,
        ORDER_CONSTRAINT_ORDER_CREATION_PUBLISHES_ORDER_CREATED,
        ORDER_CONSTRAINT_ORDER_CANCELLATION_RELEASES_ALLOCATIONS,
    ),
    properties=(ORDER_PROPERTY_ORDER_REQUIRES_AT_LEAST_ONE_ORDER_LINE,),
    events=(ORDER_EVENT_ORDER_CREATED, ORDER_EVENT_ORDER_CANCELLED),
    depends_on=(ORDER_MODEL_MONEY, ORDER_MODEL_ORDER_LINE),
)

ORDER_MODEL_BATCH = DomainModel(
    id="ORDER_MODEL_BATCH",
    name="Batch",
    model_type="Entity",
    scope="@order",
    fields=(
        ModelField("ORDER_MODEL_BATCH_FIELD_REFERENCE", "reference", "str", "고유 식별자"),
        ModelField("ORDER_MODEL_BATCH_FIELD_SKU", "sku", "str", ""),
        ModelField("ORDER_MODEL_BATCH_FIELD_PURCHASED_QUANTITY", "purchased_quantity", "int", "> 0"),
        ModelField("ORDER_MODEL_BATCH_FIELD_ETA", "eta", "date | None", ""),
        ModelField("ORDER_MODEL_BATCH_FIELD_ALLOCATIONS", "allocations", "set[OrderLine]", ""),
        ModelField(
            "ORDER_MODEL_BATCH_FIELD_PENDING_EVENTS",
            "pending_events",
            "list[OutOfStock]",
            "",
        ),
    ),
    doc_file="docs/order/batch.md",
    constraints=(
        ORDER_CONSTRAINT_BATCH_AVAILABLE_QUANTITY_NON_NEGATIVE,
        ORDER_CONSTRAINT_BATCH_ALLOCATION_IDEMPOTENT,
        ORDER_CONSTRAINT_ALLOCATION_REQUIRES_MATCHING_SKU,
        ORDER_CONSTRAINT_ORDER_CANCELLATION_RELEASES_ALLOCATIONS,
    ),
    properties=(
        ORDER_PROPERTY_BATCH_AVAILABLE_QUANTITY_NON_NEGATIVE,
        ORDER_PROPERTY_BATCH_ALLOCATION_IDEMPOTENT,
        ORDER_PROPERTY_ALLOCATION_REQUIRES_MATCHING_SKU,
    ),
    events=(ORDER_EVENT_ORDER_CANCELLED, ORDER_EVENT_OUT_OF_STOCK),
    depends_on=(ORDER_MODEL_ORDER_LINE,),
)

MODELS: tuple[DomainModel, ...] = (
    ORDER_MODEL_MONEY,
    ORDER_MODEL_ORDER_LINE,
    ORDER_MODEL_ORDER,
    ORDER_MODEL_BATCH,
)

__all__ = [
    "MODELS",
    "ORDER_MODEL_BATCH",
    "ORDER_MODEL_MONEY",
    "ORDER_MODEL_ORDER",
    "ORDER_MODEL_ORDER_LINE",
]