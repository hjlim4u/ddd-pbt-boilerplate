"""도메인 예외."""


class CurrencyMismatchError(ValueError):
    """ORD_FMT_MONEY_CURRENCY_ISO4217_UPPER: 서로 다른 통화 간 연산 시 발생."""

    def __init__(self, left: str, right: str) -> None:
        super().__init__(f"Cannot operate on {left} and {right}")
        self.left = left
        self.right = right


class CannotAllocateError(Exception):
    """ORD_INV_BATCH_AVAILABLE_QUANTITY_NONNEG, ORD_POL_ALLOC_REQUIRES_MATCHING_SKU: 배정 불가 시 발생."""

    def __init__(self, sku: str, reason: str) -> None:
        super().__init__(f"Cannot allocate {sku}: {reason}")
        self.sku = sku
        self.reason = reason


class InvalidOrderError(ValueError):
    """ORD_INV_ORDER_REQUIRES_ORDER_LINE: 유효하지 않은 Order 생성 시 발생."""
