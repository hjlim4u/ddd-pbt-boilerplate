"""도메인 서비스."""

from datetime import date

from src.domain.exceptions import CannotAllocateError
from src.domain.models import Batch, OrderLine


def allocate(line: OrderLine, batches: list[Batch]) -> str:
    """POL-02: SKU 일치하는 Batch 중 ETA 빠른 순으로 배정. INV-01 보장.

    In-stock(eta=None)이 shipment보다 우선한다.
    """
    sorted_batches = sorted(
        (b for b in batches if b.can_allocate(line)),
        key=lambda b: (b.eta is not None, b.eta or date.min),
    )
    if not sorted_batches:
        raise CannotAllocateError(line.sku, "no available batch")
    batch = sorted_batches[0]
    batch.allocate(line)
    return batch.reference


def cancel_order(order_id: str, batches: list[Batch]) -> list[OrderLine]:
    """POL-03: 주문 취소 시 모든 배정 해제."""
    deallocated: list[OrderLine] = []
    for batch in batches:
        to_remove = {
            line for line in batch._allocations if line.order_id == order_id
        }
        for line in to_remove:
            batch.deallocate(line)
            deallocated.append(line)
    return deallocated
