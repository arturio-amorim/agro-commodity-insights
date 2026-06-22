"""Time-series indicators in pure Python (no pandas/numpy) — easy to test."""
from __future__ import annotations

import math
from typing import List


def sma(values: List[float], window: int) -> float:
    """Simple moving average of the last `window` values."""
    if window <= 0:
        raise ValueError("window must be > 0")
    if not values:
        raise ValueError("values must not be empty")
    window_values = values[-window:]
    return sum(window_values) / len(window_values)


def pct_change(values: List[float], periods: int = 1) -> float:
    """Percent change over `periods` steps (latest vs `periods` ago)."""
    if periods <= 0 or len(values) <= periods:
        return 0.0
    old, new = values[-periods - 1], values[-1]
    return (new - old) / old * 100 if old else 0.0


def returns(values: List[float]) -> List[float]:
    return [
        (values[i] - values[i - 1]) / values[i - 1]
        for i in range(1, len(values))
        if values[i - 1]
    ]


def volatility(values: List[float]) -> float:
    """Std dev of period-over-period returns, as a percentage."""
    r = returns(values)
    if len(r) < 2:
        return 0.0
    mean = sum(r) / len(r)
    variance = sum((x - mean) ** 2 for x in r) / (len(r) - 1)
    return math.sqrt(variance) * 100


def trend(values: List[float], short: int = 5, long: int = 20) -> str:
    """Direction from a short vs long SMA crossover."""
    if len(values) < 2:
        return "flat"
    s, l = sma(values, short), sma(values, long)
    if s > l * 1.001:
        return "up"
    if s < l * 0.999:
        return "down"
    return "flat"
