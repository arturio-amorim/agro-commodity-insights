"""Tests for the pure-Python indicators."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pytest  # noqa: E402

from agromarket.indicators import pct_change, sma, trend, volatility  # noqa: E402


def test_sma():
    assert sma([1, 2, 3, 4, 5], 5) == 3.0
    assert sma([2, 4, 6], 2) == 5.0
    assert sma([10], 5) == 10.0  # fewer values than window


def test_sma_invalid_window():
    with pytest.raises(ValueError):
        sma([1, 2, 3], 0)


def test_pct_change():
    assert pct_change([100, 110]) == 10.0
    assert round(pct_change([100, 110, 121], 1), 2) == 10.0
    assert pct_change([100], 1) == 0.0  # not enough data


def test_volatility_constant_series_is_zero():
    assert volatility([5, 5, 5, 5]) == 0.0


def test_volatility_positive_for_varying_series():
    assert volatility([100, 110, 90, 120, 80]) > 0


def test_trend_up_and_down():
    rising = list(range(1, 31))
    falling = list(range(30, 0, -1))
    assert trend(rising) == "up"
    assert trend(falling) == "down"


def test_trend_flat_for_constant():
    assert trend([100] * 25) == "flat"
