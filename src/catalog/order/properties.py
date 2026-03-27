"""@order scope properties."""

from src.catalog.types import Property

from .constraints import (
    ORD_FMT_MONEY_CURRENCY_ISO4217_UPPER,
    ORD_FMT_ORDER_LINE_SKU_UPPER_ALNUM_HYPHEN_MAX20,
    ORD_INV_BATCH_ALLOC_IDEMPOTENT,
    ORD_INV_BATCH_AVAILABLE_QUANTITY_NONNEG,
    ORD_INV_MONEY_AMOUNT_NONNEG,
    ORD_INV_ORDER_REQUIRES_ORDER_LINE,
    ORD_POL_ALLOC_REQUIRES_MATCHING_SKU,
)


ORD_P_MONEY_SERIALIZATION_ROUND_TRIP = Property(
    id="ORD_P_MONEY_SERIALIZATION_ROUND_TRIP",
    name="Money 직렬화 왕복",
    source=(ORD_INV_MONEY_AMOUNT_NONNEG, ORD_FMT_MONEY_CURRENCY_ISO4217_UPPER),
    category="round-trip",
    description="Money를 직렬화 후 역직렬화하면 원래 값과 동일",
    test_mode="PBT",
    test_file="tests/properties/test_money_properties.py",
)

ORD_P_MONEY_ADDITION_COMMUTATIVE = Property(
    id="ORD_P_MONEY_ADDITION_COMMUTATIVE",
    name="Money 덧셈 교환법칙",
    source=(ORD_INV_MONEY_AMOUNT_NONNEG,),
    category="invariant",
    description="같은 통화의 Money 덧셈은 교환법칙이 성립한다",
    test_mode="PBT",
    test_file="tests/properties/test_money_properties.py",
)

ORD_P_BATCH_AVAILABLE_QUANTITY_NONNEG = Property(
    id="ORD_P_BATCH_AVAILABLE_QUANTITY_NONNEG",
    name="Batch 가용 수량 비음수",
    source=(ORD_INV_BATCH_AVAILABLE_QUANTITY_NONNEG,),
    category="invariant",
    description="어떤 유효한 배정 시퀀스 이후에도 Batch.available_quantity >= 0",
    test_mode="PBT",
    test_file="tests/properties/test_batch_properties.py",
)

ORD_P_ORDER_REQUIRES_ORDER_LINE = Property(
    id="ORD_P_ORDER_REQUIRES_ORDER_LINE",
    name="Order 최소 항목",
    source=(ORD_INV_ORDER_REQUIRES_ORDER_LINE,),
    category="invariant",
    description="유효한 Order는 항상 len(order_lines) >= 1",
    test_mode="Mixed",
    test_file="tests/unit/test_order.py",
)

ORD_P_BATCH_ALLOC_IDEMPOTENT = Property(
    id="ORD_P_BATCH_ALLOC_IDEMPOTENT",
    name="배정 멱등성",
    source=(ORD_INV_BATCH_ALLOC_IDEMPOTENT,),
    category="idempotence",
    description="같은 OrderLine을 같은 Batch에 두 번 배정해도 상태 변화 없음",
    test_mode="PBT",
    test_file="tests/properties/test_batch_properties.py",
)

ORD_P_ALLOC_REQUIRES_MATCHING_SKU = Property(
    id="ORD_P_ALLOC_REQUIRES_MATCHING_SKU",
    name="SKU 일치 검증",
    source=(ORD_POL_ALLOC_REQUIRES_MATCHING_SKU,),
    category="policy",
    description="SKU가 다른 OrderLine은 Batch에 배정할 수 없다",
    test_mode="PBT",
    test_file="tests/properties/test_batch_properties.py",
)

ORD_P_ORDER_LINE_SKU_FORMAT_VALIDATION = Property(
    id="ORD_P_ORDER_LINE_SKU_FORMAT_VALIDATION",
    name="OrderLine SKU 형식 검증",
    source=(ORD_FMT_ORDER_LINE_SKU_UPPER_ALNUM_HYPHEN_MAX20,),
    category="invariant",
    description="유효한 SKU는 생성 가능하고, 형식이 맞지 않는 SKU는 거부된다",
    test_mode="PBT",
    test_file="tests/properties/test_orderline_properties.py",
)

PROPERTIES: tuple[Property, ...] = (
    ORD_P_MONEY_SERIALIZATION_ROUND_TRIP,
    ORD_P_MONEY_ADDITION_COMMUTATIVE,
    ORD_P_BATCH_AVAILABLE_QUANTITY_NONNEG,
    ORD_P_ORDER_REQUIRES_ORDER_LINE,
    ORD_P_BATCH_ALLOC_IDEMPOTENT,
    ORD_P_ALLOC_REQUIRES_MATCHING_SKU,
    ORD_P_ORDER_LINE_SKU_FORMAT_VALIDATION,
)

__all__ = [
    "ORD_P_ALLOC_REQUIRES_MATCHING_SKU",
    "ORD_P_BATCH_ALLOC_IDEMPOTENT",
    "ORD_P_BATCH_AVAILABLE_QUANTITY_NONNEG",
    "ORD_P_MONEY_ADDITION_COMMUTATIVE",
    "ORD_P_MONEY_SERIALIZATION_ROUND_TRIP",
    "ORD_P_ORDER_LINE_SKU_FORMAT_VALIDATION",
    "ORD_P_ORDER_REQUIRES_ORDER_LINE",
    "PROPERTIES",
]
