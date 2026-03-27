"""Money Property-Based Tests. P-001 (round-trip), P-002 (commutativity)."""

from decimal import Decimal

import pytest
from hypothesis import assume, given

from src.domain.exceptions import CurrencyMismatchError
from src.domain.models import Money
from tests.conftest import valid_money

# ──────────────────────────────────────────────
# P-001: Money 직렬화 왕복 (INV-03, FMT-01)
# ──────────────────────────────────────────────


@given(money=valid_money())
def test_money_roundtrip_serialization(money: Money) -> None:
    """Money → dict → Money 왕복 시 값이 보존된다."""
    serialized = money.model_dump()
    restored = Money.model_validate(serialized)
    assert restored == money


@given(money=valid_money())
def test_money_json_roundtrip(money: Money) -> None:
    """Money → JSON str → Money 왕복."""
    json_str = money.model_dump_json()
    restored = Money.model_validate_json(json_str)
    assert restored == money


# ──────────────────────────────────────────────
# P-002: Money 덧셈 교환법칙 (INV-03)
# ──────────────────────────────────────────────


@given(m1=valid_money(), m2=valid_money())
def test_money_addition_is_commutative(m1: Money, m2: Money) -> None:
    """같은 통화의 덧셈은 교환법칙이 성립한다."""
    assume(m1.currency == m2.currency)
    assert m1 + m2 == m2 + m1


@given(m1=valid_money(), m2=valid_money())
def test_money_addition_preserves_non_negative(m1: Money, m2: Money) -> None:
    """INV-03: 덧셈 결과도 0 이상이다."""
    assume(m1.currency == m2.currency)
    result = m1 + m2
    assert result.amount >= 0


@given(money=valid_money())
def test_money_add_zero_identity(money: Money) -> None:
    """0을 더하면 원래 값과 같다."""
    zero = Money(amount=Decimal("0"), currency=money.currency)
    assert money + zero == money


@given(m1=valid_money(), m2=valid_money())
def test_money_different_currency_raises(m1: Money, m2: Money) -> None:
    """다른 통화 간 연산은 CurrencyMismatchError."""
    assume(m1.currency != m2.currency)
    with pytest.raises(CurrencyMismatchError):
        m1 + m2
