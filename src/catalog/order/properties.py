"""@order scope properties."""

from src.catalog.types import Property

from .constraints import (
    ORDER_CONSTRAINT_ALLOCATION_REQUIRES_MATCHING_SKU,
    ORDER_CONSTRAINT_BATCH_ALLOCATION_IDEMPOTENT,
    ORDER_CONSTRAINT_BATCH_AVAILABLE_QUANTITY_NON_NEGATIVE,
    ORDER_CONSTRAINT_CURRENCY_IS_ISO_4217_UPPERCASE,
    ORDER_CONSTRAINT_MONEY_AMOUNT_NON_NEGATIVE,
    ORDER_CONSTRAINT_ORDER_REQUIRES_AT_LEAST_ONE_ORDER_LINE,
    ORDER_CONSTRAINT_SKU_IS_UPPERCASE_ALNUM_HYPHEN_MAX_20,
)


ORDER_PROPERTY_MONEY_SERIALIZATION_ROUND_TRIP = Property(
    id="ORDER_PROPERTY_MONEY_SERIALIZATION_ROUND_TRIP",
    name="Money 직렬화 왕복",
    source=(ORDER_CONSTRAINT_MONEY_AMOUNT_NON_NEGATIVE, ORDER_CONSTRAINT_CURRENCY_IS_ISO_4217_UPPERCASE),
    category="round-trip",
    description="Money를 직렬화 후 역직렬화하면 원래 값과 동일",
    test_mode="PBT",
    test_file="tests/properties/test_money_properties.py",
)

ORDER_PROPERTY_MONEY_ADDITION_IS_COMMUTATIVE = Property(
    id="ORDER_PROPERTY_MONEY_ADDITION_IS_COMMUTATIVE",
    name="Money 덧셈 교환법칙",
    source=(ORDER_CONSTRAINT_MONEY_AMOUNT_NON_NEGATIVE,),
    category="invariant",
    description="같은 통화의 Money 덧셈은 교환법칙이 성립한다",
    test_mode="PBT",
    test_file="tests/properties/test_money_properties.py",
)

ORDER_PROPERTY_BATCH_AVAILABLE_QUANTITY_NON_NEGATIVE = Property(
    id="ORDER_PROPERTY_BATCH_AVAILABLE_QUANTITY_NON_NEGATIVE",
    name="Batch 가용 수량 비음수",
    source=(ORDER_CONSTRAINT_BATCH_AVAILABLE_QUANTITY_NON_NEGATIVE,),
    category="invariant",
    description="어떤 유효한 배정 시퀀스 이후에도 Batch.available_quantity >= 0",
    test_mode="PBT",
    test_file="tests/properties/test_batch_properties.py",
)

ORDER_PROPERTY_ORDER_REQUIRES_AT_LEAST_ONE_ORDER_LINE = Property(
    id="ORDER_PROPERTY_ORDER_REQUIRES_AT_LEAST_ONE_ORDER_LINE",
    name="Order 최소 항목",
    source=(ORDER_CONSTRAINT_ORDER_REQUIRES_AT_LEAST_ONE_ORDER_LINE,),
    category="invariant",
    description="유효한 Order는 항상 len(order_lines) >= 1",
    test_mode="Mixed",
    test_file="tests/unit/test_order.py",
)

ORDER_PROPERTY_BATCH_ALLOCATION_IDEMPOTENT = Property(
    id="ORDER_PROPERTY_BATCH_ALLOCATION_IDEMPOTENT",
    name="배정 멱등성",
    source=(ORDER_CONSTRAINT_BATCH_ALLOCATION_IDEMPOTENT,),
    category="idempotence",
    description="같은 OrderLine을 같은 Batch에 두 번 배정해도 상태 변화 없음",
    test_mode="PBT",
    test_file="tests/properties/test_batch_properties.py",
)

ORDER_PROPERTY_ALLOCATION_REQUIRES_MATCHING_SKU = Property(
    id="ORDER_PROPERTY_ALLOCATION_REQUIRES_MATCHING_SKU",
    name="SKU 일치 검증",
    source=(ORDER_CONSTRAINT_ALLOCATION_REQUIRES_MATCHING_SKU,),
    category="policy",
    description="SKU가 다른 OrderLine은 Batch에 배정할 수 없다",
    test_mode="PBT",
    test_file="tests/properties/test_batch_properties.py",
)

ORDER_PROPERTY_ORDER_LINE_SKU_FORMAT_VALIDATION = Property(
    id="ORDER_PROPERTY_ORDER_LINE_SKU_FORMAT_VALIDATION",
    name="OrderLine SKU 형식 검증",
    source=(ORDER_CONSTRAINT_SKU_IS_UPPERCASE_ALNUM_HYPHEN_MAX_20,),
    category="invariant",
    description="유효한 SKU는 생성 가능하고, 형식이 맞지 않는 SKU는 거부된다",
    test_mode="PBT",
    test_file="tests/properties/test_orderline_properties.py",
)

PROPERTIES: tuple[Property, ...] = (
    ORDER_PROPERTY_MONEY_SERIALIZATION_ROUND_TRIP,
    ORDER_PROPERTY_MONEY_ADDITION_IS_COMMUTATIVE,
    ORDER_PROPERTY_BATCH_AVAILABLE_QUANTITY_NON_NEGATIVE,
    ORDER_PROPERTY_ORDER_REQUIRES_AT_LEAST_ONE_ORDER_LINE,
    ORDER_PROPERTY_BATCH_ALLOCATION_IDEMPOTENT,
    ORDER_PROPERTY_ALLOCATION_REQUIRES_MATCHING_SKU,
    ORDER_PROPERTY_ORDER_LINE_SKU_FORMAT_VALIDATION,
)

__all__ = [
    "ORDER_PROPERTY_ALLOCATION_REQUIRES_MATCHING_SKU",
    "ORDER_PROPERTY_BATCH_ALLOCATION_IDEMPOTENT",
    "ORDER_PROPERTY_BATCH_AVAILABLE_QUANTITY_NON_NEGATIVE",
    "ORDER_PROPERTY_MONEY_ADDITION_IS_COMMUTATIVE",
    "ORDER_PROPERTY_MONEY_SERIALIZATION_ROUND_TRIP",
    "ORDER_PROPERTY_ORDER_LINE_SKU_FORMAT_VALIDATION",
    "ORDER_PROPERTY_ORDER_REQUIRES_AT_LEAST_ONE_ORDER_LINE",
    "PROPERTIES",
]