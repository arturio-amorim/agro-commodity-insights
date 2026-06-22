"""Domain models (pure dataclasses)."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PricePoint:
    date: str
    price: float


@dataclass
class MarketSummary:
    commodity: str
    n: int
    latest: float
    change_1d_pct: float
    change_30d_pct: float
    sma_short: float
    sma_long: float
    volatility_pct: float
    trend: str        # up | down | flat
    high: float
    low: float

    def as_dict(self) -> dict:
        return self.__dict__.copy()
