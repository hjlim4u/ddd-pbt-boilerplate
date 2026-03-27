"""도메인 예외."""


class CurrencyMismatchError(ValueError):
    """order_constraint_money_amount_non_negative: 서로 다른 통화 간 연산 시 발생."""

    def __init__(self, left: str, right: str) -> None:
        super().__init__(f"Cannot operate on {left} and {right}")
        self.left = left
        self.right = right


class CannotAllocateError(Exception):
    """INorder_model_money, order_constraint_allocation_requires_matching_sku: 배정 불가 시 발생."""

    def __init__(self, sku: str, reason: str) -> None:
        super().__init__(f"Cannot allocate {sku}: {reason}")
        self.sku = sku
        self.reason = reason


class InvalidOrderError(ValueError):
    """INorder_model_order_line: 유효하지 않은 Order 생성 시 발생."""
