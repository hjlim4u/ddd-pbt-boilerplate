"""Batch PBT. order_property_batch_available_quantity_non_negative (non-negative), order_property_batch_allocation_idempotent (idempotence), order_property_allocation_requires_matching_sku (SKU)."""

from datetime import date

from hypothesis import assume, given
from hypothesis import strategies as st
from hypothesis.stateful import RuleBasedStateMachine, invariant, rule

from src.domain.models import Batch, OrderLine

# ──────────────────────────────────────────────
# order_property_batch_available_quantity_non_negative: Batch 가용 수량 비음수 — stateful (INorder_model_money)
# ──────────────────────────────────────────────


class BatchAllocationMachine(RuleBasedStateMachine):
    """INorder_model_money: 어떤 배정/해제 시퀀스 이후에도 available_quantity >= 0."""

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
# order_property_batch_allocation_idempotent: 배정 멱등성 (order_constraint_batch_allocation_idempotent)
# ──────────────────────────────────────────────


@given(qty=st.integers(min_value=1, max_value=50))
def test_allocation_is_idempotent(qty: int) -> None:
    """order_constraint_batch_allocation_idempotent: 같은 라인을 두 번 배정해도 가용 수량은 한 번만 감소."""
    batch = Batch("B-001", "WIDGET", 100, eta=None)
    line = OrderLine(order_id="O-001", sku="WIDGET", quantity=qty)
    batch.allocate(line)
    qty_after_first = batch.available_quantity
    batch.allocate(line)
    assert batch.available_quantity == qty_after_first


# ──────────────────────────────────────────────
# order_property_allocation_requires_matching_sku: SKU 일치 검증 (order_constraint_allocation_requires_matching_sku)
# ──────────────────────────────────────────────


@given(
    batch_sku=st.from_regex(r"[A-Z0-9\-]{3,10}", fullmatch=True),
    line_sku=st.from_regex(r"[A-Z0-9\-]{3,10}", fullmatch=True),
    qty=st.integers(min_value=1, max_value=50),
)
def test_cannot_allocate_mismatched_sku(
    batch_sku: str, line_sku: str, qty: int
) -> None:
    """order_constraint_allocation_requires_matching_sku: SKU가 다르면 can_allocate는 False."""
    assume(batch_sku != line_sku)
    batch = Batch("B-001", batch_sku, 100, eta=None)
    line = OrderLine(order_id="O-001", sku=line_sku, quantity=qty)
    assert batch.can_allocate(line) is False


@given(
    sku=st.from_regex(r"[A-Z0-9\-]{3,10}", fullmatch=True),
    qty=st.integers(min_value=1, max_value=50),
)
def test_can_allocate_matching_sku(sku: str, qty: int) -> None:
    """order_constraint_allocation_requires_matching_sku: SKU가 같고 수량이 충분하면 can_allocate는 True."""
    batch = Batch("B-001", sku, 100, eta=None)
    line = OrderLine(order_id="O-001", sku=sku, quantity=qty)
    assert batch.can_allocate(line) is True
