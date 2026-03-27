"""OrderLine PBT. order_property_order_line_sku_format_validation (SKU format validation)."""

import re

import pytest
from hypothesis import assume, given
from hypothesis import strategies as st
from pydantic import ValidationError

from src.domain.models import OrderLine


@given(
    sku=st.from_regex(r"[A-Z0-9\-]{1,20}", fullmatch=True),
    qty=st.integers(min_value=1, max_value=100),
)
def test_orderline_accepts_valid_sku(sku: str, qty: int) -> None:
    """order_constraint_sku_is_uppercase_alnum_hyphen_max_20: 유효한 SKU 형식은 OrderLine 생성에 성공한다."""
    line = OrderLine(order_id="O-001", sku=sku, quantity=qty)
    assert line.sku == sku


@given(
    sku=st.text(
        alphabet=st.characters(blacklist_categories=("Cs",)),
        min_size=1,
        max_size=25,
    ),
    qty=st.integers(min_value=1, max_value=100),
)
def test_orderline_rejects_invalid_sku(sku: str, qty: int) -> None:
    """order_constraint_sku_is_uppercase_alnum_hyphen_max_20: 형식이 맞지 않는 SKU는 거부된다."""
    assume(not bool(re.fullmatch(r"[A-Z0-9\-]{1,20}", sku)))
    with pytest.raises(ValidationError):
        OrderLine(order_id="O-001", sku=sku, quantity=qty)
