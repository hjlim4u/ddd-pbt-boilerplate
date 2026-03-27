"""@order 스코프 도메인 카탈로그.

docs/ 문서를 Source of Truth로 삼아 작성된 구조화된 도메인 지식.
구현 코드(src/domain/)에 의존하지 않는다.
"""

from src.catalog.types import (
    Constraint,
    DomainEvent,
    DomainModel,
    GlossaryTerm,
    ModelField,
    Property,
)

# ──────────────────────────────────────────────
# Models
# ──────────────────────────────────────────────

ORDER = DomainModel(
    id="E-01",
    name="Order",
    model_type="Entity",
    scope="@order",
    fields=(
        ModelField("id", "str", "UUID"),
        ModelField("customer_id", "str", ""),
        ModelField("order_lines", "list[OrderLine]", "최소 1개"),
        ModelField("created_at", "datetime", ""),
        ModelField("pending_events", "list[OrderCreated | OrderCancelled]", ""),
    ),
    doc_file="docs/order/order.md",
    constraints=("INV-02", "POL-01"),
    properties=("P-004",),
    events=("EV-01", "EV-02"),
    depends_on=("V-01", "V-02"),
)

BATCH = DomainModel(
    id="E-02",
    name="Batch",
    model_type="Entity",
    scope="@order",
    fields=(
        ModelField("reference", "str", "고유 식별자"),
        ModelField("sku", "str", ""),
        ModelField("purchased_quantity", "int", "> 0"),
        ModelField("eta", "date | None", ""),
        ModelField("allocations", "set[OrderLine]", ""),
        ModelField("pending_events", "list[OutOfStock]", ""),
    ),
    doc_file="docs/order/batch.md",
    constraints=("INV-01", "INV-04", "POL-02", "POL-03"),
    properties=("P-003", "P-005", "P-006"),
    events=("EV-03",),
    depends_on=("V-02",),
)

MONEY = DomainModel(
    id="V-01",
    name="Money",
    model_type="ValueObject",
    scope="@order",
    fields=(
        ModelField("amount", "Decimal", ">= 0, 소수점 2자리"),
        ModelField("currency", "str", "ISO 4217 3자리"),
    ),
    doc_file="docs/order/money.md",
    constraints=("INV-03", "FMT-01"),
    properties=("P-001", "P-002"),
    events=(),
    depends_on=(),
)

ORDER_LINE = DomainModel(
    id="V-02",
    name="OrderLine",
    model_type="ValueObject",
    scope="@order",
    fields=(
        ModelField("order_id", "str", ""),
        ModelField("sku", "str", "대문자 영숫자+하이픈, 최대 20자"),
        ModelField("quantity", "int", "> 0"),
    ),
    doc_file="docs/order/orderline.md",
    constraints=("FMT-02",),
    properties=("P-007",),
    events=(),
    depends_on=(),
)

MODELS: tuple[DomainModel, ...] = (ORDER, BATCH, MONEY, ORDER_LINE)

# ──────────────────────────────────────────────
# Constraints
# ──────────────────────────────────────────────

INV_01 = Constraint(
    id="INV-01",
    category="invariant",
    description="Batch의 가용 수량은 절대 음수가 될 수 없다",
    applies_to=("E-02",),
    properties=("P-003",),
)

INV_02 = Constraint(
    id="INV-02",
    category="invariant",
    description="Order는 최소 1개의 OrderLine을 가져야 한다",
    applies_to=("E-01",),
    properties=("P-004",),
)

INV_03 = Constraint(
    id="INV-03",
    category="invariant",
    description="Money의 amount는 0 이상이어야 한다",
    applies_to=("V-01",),
    properties=("P-001", "P-002"),
)

INV_04 = Constraint(
    id="INV-04",
    category="invariant",
    description="같은 OrderLine을 같은 Batch에 두 번 배정하면 두 번째는 무시된다 (멱등성)",
    applies_to=("E-02",),
    properties=("P-005",),
)

POL_01 = Constraint(
    id="POL-01",
    category="policy",
    description="Order 생성 시 OrderCreated 이벤트가 발행된다",
    applies_to=("E-01",),
    properties=(),
)

POL_02 = Constraint(
    id="POL-02",
    category="policy",
    description="배정 시 SKU가 일치해야 한다",
    applies_to=("E-02",),
    properties=("P-006",),
)

POL_03 = Constraint(
    id="POL-03",
    category="policy",
    description="주문 취소 시 모든 배정이 해제되어야 한다",
    applies_to=("E-01", "E-02"),
    properties=(),
)

FMT_01 = Constraint(
    id="FMT-01",
    category="format",
    description="Currency는 ISO 4217 3자리 대문자 코드",
    applies_to=("V-01",),
    properties=("P-001",),
)

FMT_02 = Constraint(
    id="FMT-02",
    category="format",
    description="SKU는 대문자 영숫자 + 하이픈, 최대 20자",
    applies_to=("V-02",),
    properties=("P-007",),
)

CONSTRAINTS: tuple[Constraint, ...] = (
    INV_01, INV_02, INV_03, INV_04,
    POL_01, POL_02, POL_03,
    FMT_01, FMT_02,
)

# ──────────────────────────────────────────────
# Properties
# ──────────────────────────────────────────────

P_001 = Property(
    id="P-001",
    name="Money 직렬화 왕복",
    source=("INV-03", "FMT-01"),
    models=("V-01",),
    category="round-trip",
    description="Money를 직렬화 후 역직렬화하면 원래 값과 동일",
    test_mode="PBT",
    test_file="tests/properties/test_money_properties.py",
)

P_002 = Property(
    id="P-002",
    name="Money 덧셈 교환법칙",
    source=("INV-03",),
    models=("V-01",),
    category="invariant",
    description="같은 통화의 Money 덧셈은 교환법칙이 성립한다",
    test_mode="PBT",
    test_file="tests/properties/test_money_properties.py",
)

P_003 = Property(
    id="P-003",
    name="Batch 가용 수량 비음수",
    source=("INV-01",),
    models=("E-02",),
    category="invariant",
    description="어떤 유효한 배정 시퀀스 이후에도 Batch.available_quantity >= 0",
    test_mode="PBT",
    test_file="tests/properties/test_batch_properties.py",
)

P_004 = Property(
    id="P-004",
    name="Order 최소 항목",
    source=("INV-02",),
    models=("E-01",),
    category="invariant",
    description="유효한 Order는 항상 len(order_lines) >= 1",
    test_mode="Mixed",
    test_file="tests/unit/test_order.py",
)

P_005 = Property(
    id="P-005",
    name="배정 멱등성",
    source=("INV-04",),
    models=("E-02",),
    category="idempotence",
    description="같은 OrderLine을 같은 Batch에 두 번 배정해도 상태 변화 없음",
    test_mode="PBT",
    test_file="tests/properties/test_batch_properties.py",
)

P_006 = Property(
    id="P-006",
    name="SKU 일치 검증",
    source=("POL-02",),
    models=("E-02", "V-02"),
    category="policy",
    description="SKU가 다른 OrderLine은 Batch에 배정할 수 없다",
    test_mode="PBT",
    test_file="tests/properties/test_batch_properties.py",
)

P_007 = Property(
    id="P-007",
    name="OrderLine SKU 형식 검증",
    source=("FMT-02",),
    models=("V-02",),
    category="invariant",
    description="유효한 SKU는 생성 가능하고, 형식이 맞지 않는 SKU는 거부된다",
    test_mode="PBT",
    test_file="tests/properties/test_orderline_properties.py",
)

PROPERTIES: tuple[Property, ...] = (P_001, P_002, P_003, P_004, P_005, P_006, P_007)

# ──────────────────────────────────────────────
# Events
# ──────────────────────────────────────────────

EV_01 = DomainEvent(
    id="EV-01",
    name="OrderCreated",
    scope="@order",
    payload=("order_id", "customer_id", "order_lines[]", "timestamp"),
    trigger="고객이 결제 완료 시",
    subsequent="재고 배정 시작",
    related_models=("E-01",),
)

EV_02 = DomainEvent(
    id="EV-02",
    name="OrderCancelled",
    scope="@order",
    payload=("order_id", "reason", "timestamp"),
    trigger="고객 취소 또는 결제 실패",
    subsequent="배정된 재고 해제",
    related_models=("E-01", "E-02"),
)

EV_03 = DomainEvent(
    id="EV-03",
    name="OutOfStock",
    scope="@order",
    payload=("sku", "requested_quantity", "timestamp"),
    trigger="배정 시 가용 수량 부족",
    subsequent="주문자에게 알림",
    related_models=("E-02",),
)

EVENTS: tuple[DomainEvent, ...] = (EV_01, EV_02, EV_03)

# ──────────────────────────────────────────────
# Glossary
# ──────────────────────────────────────────────

GLOSSARY: tuple[GlossaryTerm, ...] = (
    GlossaryTerm(
        id="G-01",
        term="Order",
        definition="고객이 결제를 완료한 구매 건. '요청'이나 '장바구니'와 다름.",
    ),
    GlossaryTerm(
        id="G-02",
        term="OrderLine",
        definition="Order 안의 개별 상품 항목. SKU + 수량으로 구성. '장바구니 항목'과 다름.",
    ),
    GlossaryTerm(
        id="G-03",
        term="Batch",
        definition="창고에 입고된 상품 묶음. reference로 식별. '주문'과 다름.",
    ),
    GlossaryTerm(
        id="G-04",
        term="Allocation",
        definition="OrderLine을 특정 Batch에 배정하는 행위. 가용 수량을 감소시킴.",
    ),
    GlossaryTerm(
        id="G-05",
        term="Money",
        definition="금액 + 통화의 불변 조합. 단순 숫자가 아니라 통화 정보를 포함.",
    ),
    GlossaryTerm(
        id="G-06",
        term="SKU",
        definition="Stock Keeping Unit. 상품 변형의 고유 식별자 (모델+사이즈+색상).",
    ),
)
