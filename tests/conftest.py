"""공유 Hypothesis Strategies + 프로파일 설정."""

import os
from decimal import Decimal

import hypothesis.strategies as st
from hypothesis import HealthCheck, Phase, settings

from src.domain.models import Money, OrderLine

# ──────────────────────────────────────────────
# Hypothesis 프로파일
# ──────────────────────────────────────────────

settings.register_profile(
    "dev",
    max_examples=50,
    deadline=400,
)

settings.register_profile(
    "ci",
    max_examples=300,
    deadline=None,
    suppress_health_check=[HealthCheck.too_slow],
)

settings.register_profile(
    "nightly",
    max_examples=5000,
    deadline=None,
    suppress_health_check=[HealthCheck.too_slow],
    phases=[Phase.explicit, Phase.reuse, Phase.generate, Phase.shrink],
)

settings.load_profile(os.getenv("HYPOTHESIS_PROFILE", "dev"))

# ──────────────────────────────────────────────
# 공유 Strategies
# ──────────────────────────────────────────────

CURRENCIES = ["USD", "EUR", "GBP", "KRW", "JPY"]


@st.composite
def valid_money(draw: st.DrawFn) -> Money:
    """V-01 Money 기반. INV-03 + FMT-01 충족."""
    amount = draw(
        st.decimals(
            min_value=Decimal("0"),
            max_value=Decimal("999999.99"),
            places=2,
            allow_nan=False,
            allow_infinity=False,
        )
    )
    currency = draw(st.sampled_from(CURRENCIES))
    return Money(amount=amount, currency=currency)


@st.composite
def valid_order_line(draw: st.DrawFn, sku: str | None = None) -> OrderLine:
    """V-02 OrderLine 기반. FMT-02 충족."""
    _sku = sku or draw(
        st.from_regex(r"[A-Z0-9\-]{3,20}", fullmatch=True)
    )
    qty = draw(st.integers(min_value=1, max_value=100))
    order_id = draw(st.uuids().map(str))
    return OrderLine(order_id=order_id, sku=_sku, quantity=qty)
