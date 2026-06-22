"""Summarise a price series into a MarketSummary of indicators."""
from __future__ import annotations

from typing import List

from .indicators import pct_change, sma, trend, volatility
from .models import MarketSummary


def analyze(commodity: str, prices: List[float]) -> MarketSummary:
    if not prices:
        raise ValueError("prices must not be empty")
    n = len(prices)
    return MarketSummary(
        commodity=commodity,
        n=n,
        latest=round(prices[-1], 2),
        change_1d_pct=round(pct_change(prices, 1), 2),
        change_30d_pct=round(pct_change(prices, min(30, n - 1)), 2),
        sma_short=round(sma(prices, min(5, n)), 2),
        sma_long=round(sma(prices, min(20, n)), 2),
        volatility_pct=round(volatility(prices), 2),
        trend=trend(prices),
        high=round(max(prices), 2),
        low=round(min(prices), 2),
    )
