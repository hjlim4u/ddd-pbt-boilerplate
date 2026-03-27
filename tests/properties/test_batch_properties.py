"""Batch PBT. ORD_P_BATCH_AVAILABLE_QUANTITY_NONNEG (non-negative), ORD_P_BATCH_ALLOC_IDEMPOTENT (idempotence), ORD_P_ALLOC_REQUIRES_MATCHING_SKU (SKU)."""

from datetime import date

from hypothesis import assume, given
from hypothesis import strategies as st
from hypothesis.stateful import RuleBasedStateMachine, invariant, rule

from src.domain.models import Batch, OrderLine

# ──────────────────────────────────────────────
# ORD_P_BATCH_AVAILABLE_QUANTITY_NONNEG: Batch 가용 수량 비음수 — stateful (ORD_INV_BATCH_AVAILABLE_QUANTITY_NONNEG)
# ──────────────────────────────────────────────


class BatchAllocationMachine(RuleBasedStateMachine):
    """ORD_INV_BATCH_AVAILABLE_QUANTITY_NONNEG: 어떤 배정/해제 시퀀스 이후에도 available_quantity >= 0."""

    def __init__(self) -> None:
        super().__init__()
        self.batch = Batch(
            reference="BATCH-TEST",
            sku="WIDGET",
            purchased_quantity=100,
            eta=date.today(),
        )

    @rule(qty=st.integers(min_value=1, max_value=30))
    def allocate(self, qty: int) -> None:
        line = OrderLine(order_id=f"O-{qty}", sku="WIDGET", quantity=qty)
        if self.batch.can_allocate(line):
            self.batch.allocate(line)

    @rule(qty=st.integers(min_value=1, max_value=30))
    def deallocate(self, qty: int) -> None:
        line = OrderLine(order_id=f"O-{qty}", sku="WIDGET", quantity=qty)
        self.batch.deallocate(line)

    @invariant()
    def available_never_negative(self) -> None:
        assert self.batch.available_quantity >= 0

    @invariant()
    def available_never_exceeds_purchased(self) -> None:
        assert self.batch.available_quantity <= self.batch.purchased_quantity


TestBatchAllocation = BatchAllocationMachine.TestCase


# ──────────────────────────────────────────────
# ORD_P_BATCH_ALLOC_IDEMPOTENT: 배정 멱등성 (ORD_INV_BATCH_ALLOC_IDEMPOTENT)
# ──────────────────────────────────────────────


@given(qty=st.integers(min_value=1, max_value=50))
def test_allocation_is_idempotent(qty: int) -> None:
    """ORD_INV_BATCH_ALLOC_IDEMPOTENT: 같은 라인을 두 번 배정해도 가용 수량은 한 번만 감소."""
    batch = Batch("B-001", "WIDGET", 100, eta=None)
    line = OrderLine(order_id="O-001", sku="WIDGET", quantity=qty)
    batch.allocate(line)
    qty_after_first = batch.available_quantity
    batch.allocate(line)
    assert batch.available_quantity == qty_after_first


# ──────────────────────────────────────────────
# ORD_P_ALLOC_REQUIRES_MATCHING_SKU: SKU 일치 검증 (ORD_POL_ALLOC_REQUIRES_MATCHING_SKU)
# ──────────────────────────────────────────────


@given(
    batch_sku=st.from_regex(r"[A-Z0-9\-]{3,10}", fullmatch=True),
    line_sku=st.from_regex(r"[A-Z0-9\-]{3,10}", fullmatch=True),
    qty=st.integers(min_value=1, max_value=50),
)
def test_cannot_allocate_mismatched_sku(
    batch_sku: str, line_sku: str, qty: int
) -> None:
    """ORD_POL_ALLOC_REQUIRES_MATCHING_SKU: SKU가 다르면 can_allocate는 False."""
    assume(batch_sku != line_sku)
    batch = Batch("B-001", batch_sku, 100, eta=None)
    line = OrderLine(order_id="O-001", sku=line_sku, quantity=qty)
    assert batch.can_allocate(line) is False


@given(
    sku=st.from_regex(r"[A-Z0-9\-]{3,10}", fullmatch=True),
    qty=st.integers(min_value=1, max_value=50),
)
def test_can_allocate_matching_sku(sku: str, qty: int) -> None:
    """ORD_POL_ALLOC_REQUIRES_MATCHING_SKU: SKU가 같고 수량이 충분하면 can_allocate는 True."""
    batch = Batch("B-001", sku, 100, eta=None)
    line = OrderLine(order_id="O-001", sku=sku, quantity=qty)
    assert batch.can_allocate(line) is True
