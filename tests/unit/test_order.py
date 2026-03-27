"""Order 예제 기반 TDD. P-004 (Mixed), POL-01, POL-03."""

from datetime import date

import pytest

from src.domain.exceptions import CannotAllocateError, InvalidOrderError
from src.domain.models import Batch, Order, OrderLine
from src.domain.services import allocate, cancel_order

# ──────────────────────────────────────────────
# P-004: Order 최소 항목 — Mixed의 TDD 부분 (INV-02)
# ──────────────────────────────────────────────


class TestOrderCreation:
    """INV-02: Order는 최소 1개의 OrderLine을 가져야 한다."""

    def test_empty_order_raises(self) -> None:
        with pytest.raises(InvalidOrderError):
            Order(id="O-001", customer_id="C-001", order_lines=[])

    def test_single_line_is_valid(self) -> None:
        line = OrderLine(order_id="O-001", sku="WIDGET", quantity=5)
        order = Order(id="O-001", customer_id="C-001", order_lines=[line])
        assert len(order.order_lines) == 1

    def test_multiple_lines_is_valid(self) -> None:
        lines = [
            OrderLine(order_id="O-001", sku="WIDGET", quantity=5),
            OrderLine(order_id="O-001", sku="GADGET", quantity=3),
        ]
        order = Order(id="O-001", customer_id="C-001", order_lines=lines)
        assert len(order.order_lines) == 2


# ──────────────────────────────────────────────
# POL-03: 주문 취소 시 배정 해제 — TDD 시나리오
# ──────────────────────────────────────────────


class TestCancelOrder:
    """POL-03: 주문 취소 시 모든 배정이 해제되어야 한다."""

    def test_cancel_releases_single_allocation(self) -> None:
        batch = Batch("B-001", "WIDGET", 50, eta=date(2024, 1, 1))
        line = OrderLine(order_id="O-001", sku="WIDGET", quantity=10)
        batch.allocate(line)
        assert batch.available_quantity == 40

        cancel_order("O-001", [batch])
        assert batch.available_quantity == 50

    def test_cancel_releases_across_multiple_batches(self) -> None:
        batch1 = Batch("B-001", "WIDGET", 50, eta=date(2024, 1, 1))
        batch2 = Batch("B-002", "GADGET", 30, eta=date(2024, 2, 1))
        line1 = OrderLine(order_id="O-001", sku="WIDGET", quantity=10)
        line2 = OrderLine(order_id="O-001", sku="GADGET", quantity=5)
        batch1.allocate(line1)
        batch2.allocate(line2)

        cancel_order("O-001", [batch1, batch2])

        assert batch1.available_quantity == 50
        assert batch2.available_quantity == 30

    def test_cancel_nonexistent_order_is_noop(self) -> None:
        batch = Batch("B-001", "WIDGET", 50, eta=None)
        line = OrderLine(order_id="O-001", sku="WIDGET", quantity=10)
        batch.allocate(line)

        cancel_order("O-999", [batch])
        assert batch.available_quantity == 40  # unchanged

    def test_cancel_does_not_affect_other_orders(self) -> None:
        batch = Batch("B-001", "WIDGET", 50, eta=None)
        line1 = OrderLine(order_id="O-001", sku="WIDGET", quantity=10)
        line2 = OrderLine(order_id="O-002", sku="WIDGET", quantity=15)
        batch.allocate(line1)
        batch.allocate(line2)

        cancel_order("O-001", [batch])
        assert batch.available_quantity == 35  # O-002 still allocated


# ──────────────────────────────────────────────
# 할당 서비스 — TDD 시나리오
# ──────────────────────────────────────────────


class TestAllocateService:
    """POL-02 + INV-01 통합 시나리오."""

    def test_allocate_to_earliest_batch(self) -> None:
        early = Batch("B-EARLY", "WIDGET", 50, eta=date(2024, 1, 1))
        late = Batch("B-LATE", "WIDGET", 50, eta=date(2024, 6, 1))
        line = OrderLine(order_id="O-001", sku="WIDGET", quantity=10)

        ref = allocate(line, [late, early])
        assert ref == "B-EARLY"

    def test_allocate_in_stock_before_shipment(self) -> None:
        in_stock = Batch("B-STOCK", "WIDGET", 50, eta=None)
        shipment = Batch("B-SHIP", "WIDGET", 50, eta=date(2024, 3, 1))
        line = OrderLine(order_id="O-001", sku="WIDGET", quantity=10)

        ref = allocate(line, [shipment, in_stock])
        assert ref == "B-STOCK"

    def test_allocate_raises_when_no_batch_available(self) -> None:
        batch = Batch("B-001", "WIDGET", 5, eta=None)
        line = OrderLine(order_id="O-001", sku="WIDGET", quantity=10)

        with pytest.raises(CannotAllocateError):
            allocate(line, [batch])

    def test_allocate_raises_for_sku_mismatch(self) -> None:
        batch = Batch("B-001", "WIDGET", 100, eta=None)
        line = OrderLine(order_id="O-001", sku="GADGET", quantity=10)

        with pytest.raises(CannotAllocateError):
            allocate(line, [batch])
