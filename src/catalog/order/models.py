"""@order scope models."""

from src.catalog.types import DomainModel, ModelField

from .constraints import (
    ORD_FMT_MONEY_CURRENCY_ISO4217_UPPER,
    ORD_FMT_ORDER_LINE_SKU_UPPER_ALNUM_HYPHEN_MAX20,
    ORD_INV_BATCH_ALLOC_IDEMPOTENT,
    ORD_INV_BATCH_AVAILABLE_QUANTITY_NONNEG,
    ORD_INV_MONEY_AMOUNT_NONNEG,
    ORD_INV_ORDER_REQUIRES_ORDER_LINE,
    ORD_POL_ALLOC_REQUIRES_MATCHING_SKU,
    ORD_POL_ORDER_CANCEL_RELEASES_ALLOC,
    ORD_POL_ORDER_CREATE_EMITS_ORDER_CREATED,
)
from .events import ORD_EV_ORDER_CANCELLED, ORD_EV_ORDER_CREATED, ORD_EV_OUT_OF_STOCK
from .properties import (
    ORD_P_ALLOC_REQUIRES_MATCHING_SKU,
    ORD_P_BATCH_ALLOC_IDEMPOTENT,
    ORD_P_BATCH_AVAILABLE_QUANTITY_NONNEG,
    ORD_P_MONEY_ADDITION_COMMUTATIVE,
    ORD_P_MONEY_SERIALIZATION_ROUND_TRIP,
    ORD_P_ORDER_LINE_SKU_FORMAT_VALIDATION,
    ORD_P_ORDER_REQUIRES_ORDER_LINE,
)


ORD_V_MONEY = DomainModel(
    id="ORD_V_MONEY",
    name="Money",
    model_type="ValueObject",
    scope="@order",
    fields=(
        ModelField("ORD_F_MONEY_AMOUNT", "amount", "Decimal", ">= 0, 소수점 2자리"),
        ModelField("ORD_F_MONEY_CURRENCY", "currency", "str", "ISO 4217 3자리"),
    ),
    doc_file="docs/order/money.md",
    constraints=(ORD_INV_MONEY_AMOUNT_NONNEG, ORD_FMT_MONEY_CURRENCY_ISO4217_UPPER),
    properties=(ORD_P_MONEY_SERIALIZATION_ROUND_TRIP, ORD_P_MONEY_ADDITION_COMMUTATIVE),
)

ORD_V_ORDER_LINE = DomainModel(
    id="ORD_V_ORDER_LINE",
    name="OrderLine",
    model_type="ValueObject",
    scope="@order",
    fields=(
        ModelField("ORD_F_ORDER_LINE_ORDER_ID", "order_id", "str", ""),
        ModelField("ORD_F_ORDER_LINE_SKU", "sku", "str", "대문자 영숫자+하이픈, 최대 20자"),
        ModelField("ORD_F_ORDER_LINE_QUANTITY", "quantity", "int", "> 0"),
    ),
    doc_file="docs/order/orderline.md",
    constraints=(ORD_FMT_ORDER_LINE_SKU_UPPER_ALNUM_HYPHEN_MAX20,),
    properties=(ORD_P_ORDER_LINE_SKU_FORMAT_VALIDATION,),
)

ORD_E_ORDER = DomainModel(
    id="ORD_E_ORDER",
    name="Order",
    model_type="Entity",
    scope="@order",
    fields=(
        ModelField("ORD_F_ORDER_ID", "id", "str", "UUID"),
        ModelField("ORD_F_ORDER_CUSTOMER_ID", "customer_id", "str", ""),
        ModelField("ORD_F_ORDER_ORDER_LINES", "order_lines", "list[OrderLine]", "최소 1개"),
        ModelField("ORD_F_ORDER_CREATED_AT", "created_at", "datetime", ""),
        ModelField(
            "ORD_F_ORDER_PENDING_EVENTS",
            "pending_events",
            "list[OrderCreated | OrderCancelled]",
            "",
        ),
    ),
    doc_file="docs/order/order.md",
    constraints=(
        ORD_INV_ORDER_REQUIRES_ORDER_LINE,
        ORD_POL_ORDER_CREATE_EMITS_ORDER_CREATED,
        ORD_POL_ORDER_CANCEL_RELEASES_ALLOC,
    ),
    properties=(ORD_P_ORDER_REQUIRES_ORDER_LINE,),
    events=(ORD_EV_ORDER_CREATED, ORD_EV_ORDER_CANCELLED),
    depends_on=(ORD_V_MONEY, ORD_V_ORDER_LINE),
)

ORD_E_BATCH = DomainModel(
    id="ORD_E_BATCH",
    name="Batch",
    model_type="Entity",
    scope="@order",
    fields=(
        ModelField("ORD_F_BATCH_REFERENCE", "reference", "str", "고유 식별자"),
        ModelField("ORD_F_BATCH_SKU", "sku", "str", ""),
        ModelField("ORD_F_BATCH_PURCHASED_QUANTITY", "purchased_quantity", "int", "> 0"),
        ModelField("ORD_F_BATCH_ETA", "eta", "date | None", ""),
        ModelField("ORD_F_BATCH_ALLOCATIONS", "allocations", "set[OrderLine]", ""),
        ModelField(
            "ORD_F_BATCH_PENDING_EVENTS",
            "pending_events",
            "list[OutOfStock]",
            "",
        ),
    ),
    doc_file="docs/order/batch.md",
    constraints=(
        ORD_INV_BATCH_AVAILABLE_QUANTITY_NONNEG,
        ORD_INV_BATCH_ALLOC_IDEMPOTENT,
        ORD_POL_ALLOC_REQUIRES_MATCHING_SKU,
        ORD_POL_ORDER_CANCEL_RELEASES_ALLOC,
    ),
    properties=(
        ORD_P_BATCH_AVAILABLE_QUANTITY_NONNEG,
        ORD_P_BATCH_ALLOC_IDEMPOTENT,
        ORD_P_ALLOC_REQUIRES_MATCHING_SKU,
    ),
    events=(ORD_EV_ORDER_CANCELLED, ORD_EV_OUT_OF_STOCK),
    depends_on=(ORD_V_ORDER_LINE,),
)

MODELS: tuple[DomainModel, ...] = (
    ORD_V_MONEY,
    ORD_V_ORDER_LINE,
    ORD_E_ORDER,
    ORD_E_BATCH,
)

__all__ = [
    "ORD_E_BATCH",
    "ORD_E_ORDER",
    "ORD_V_MONEY",
    "ORD_V_ORDER_LINE",
    "MODELS",
]
