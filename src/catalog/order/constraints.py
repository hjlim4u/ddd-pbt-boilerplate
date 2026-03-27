"""@order scope constraints."""

from src.catalog.types import Constraint


ORD_INV_BATCH_AVAILABLE_QUANTITY_NONNEG = Constraint(
    id="ORD_INV_BATCH_AVAILABLE_QUANTITY_NONNEG",
    category="invariant",
    description="Batch의 가용 수량은 절대 음수가 될 수 없다",
)

ORD_INV_ORDER_REQUIRES_ORDER_LINE = Constraint(
    id="ORD_INV_ORDER_REQUIRES_ORDER_LINE",
    category="invariant",
    description="Order는 최소 1개의 OrderLine을 가져야 한다",
)

ORD_INV_MONEY_AMOUNT_NONNEG = Constraint(
    id="ORD_INV_MONEY_AMOUNT_NONNEG",
    category="invariant",
    description="Money의 amount는 0 이상이어야 한다",
)

ORD_INV_BATCH_ALLOC_IDEMPOTENT = Constraint(
    id="ORD_INV_BATCH_ALLOC_IDEMPOTENT",
    category="invariant",
    description="같은 OrderLine을 같은 Batch에 두 번 배정하면 두 번째는 무시된다 (멱등성)",
)

ORD_POL_ORDER_CREATE_EMITS_ORDER_CREATED = Constraint(
    id="ORD_POL_ORDER_CREATE_EMITS_ORDER_CREATED",
    category="policy",
    description="Order 생성 시 OrderCreated 이벤트가 발행된다",
)

ORD_POL_ALLOC_REQUIRES_MATCHING_SKU = Constraint(
    id="ORD_POL_ALLOC_REQUIRES_MATCHING_SKU",
    category="policy",
    description="배정 시 SKU가 일치해야 한다",
)

ORD_POL_ORDER_CANCEL_RELEASES_ALLOC = Constraint(
    id="ORD_POL_ORDER_CANCEL_RELEASES_ALLOC",
    category="policy",
    description="주문 취소 시 모든 배정이 해제되어야 한다",
)

ORD_FMT_MONEY_CURRENCY_ISO4217_UPPER = Constraint(
    id="ORD_FMT_MONEY_CURRENCY_ISO4217_UPPER",
    category="format",
    description="Currency는 ISO 4217 3자리 대문자 코드",
)

ORD_FMT_ORDER_LINE_SKU_UPPER_ALNUM_HYPHEN_MAX20 = Constraint(
    id="ORD_FMT_ORDER_LINE_SKU_UPPER_ALNUM_HYPHEN_MAX20",
    category="format",
    description="SKU는 대문자 영숫자 + 하이픈, 최대 20자",
)

CONSTRAINTS: tuple[Constraint, ...] = (
    ORD_INV_BATCH_AVAILABLE_QUANTITY_NONNEG,
    ORD_INV_ORDER_REQUIRES_ORDER_LINE,
    ORD_INV_MONEY_AMOUNT_NONNEG,
    ORD_INV_BATCH_ALLOC_IDEMPOTENT,
    ORD_POL_ORDER_CREATE_EMITS_ORDER_CREATED,
    ORD_POL_ALLOC_REQUIRES_MATCHING_SKU,
    ORD_POL_ORDER_CANCEL_RELEASES_ALLOC,
    ORD_FMT_MONEY_CURRENCY_ISO4217_UPPER,
    ORD_FMT_ORDER_LINE_SKU_UPPER_ALNUM_HYPHEN_MAX20,
)

__all__ = [
    "CONSTRAINTS",
    "ORD_FMT_MONEY_CURRENCY_ISO4217_UPPER",
    "ORD_FMT_ORDER_LINE_SKU_UPPER_ALNUM_HYPHEN_MAX20",
    "ORD_INV_BATCH_ALLOC_IDEMPOTENT",
    "ORD_INV_BATCH_AVAILABLE_QUANTITY_NONNEG",
    "ORD_INV_MONEY_AMOUNT_NONNEG",
    "ORD_INV_ORDER_REQUIRES_ORDER_LINE",
    "ORD_POL_ALLOC_REQUIRES_MATCHING_SKU",
    "ORD_POL_ORDER_CANCEL_RELEASES_ALLOC",
    "ORD_POL_ORDER_CREATE_EMITS_ORDER_CREATED",
]
