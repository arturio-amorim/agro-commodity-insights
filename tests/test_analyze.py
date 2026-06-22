"""Tests for the analysis summary (pure)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pytest  # noqa: E402

from agromarket.analyze import analyze  # noqa: E402
from agromarket.data_io import load_csv, prices  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def test_analyze_rising_series():
    series = list(range(100, 131))  # 100..130, steadily rising
    s = analyze("Test", series)
    assert s.n == 31
    assert s.latest == 130
    assert s.high == 130
    assert s.low == 100
    assert s.trend == "up"
    assert s.change_1d_pct > 0


def test_analyze_empty_raises():
    with pytest.raises(ValueError):
        analyze("X", [])


def test_analyze_bundled_csv():
    series = prices(load_csv(str(ROOT / "data" / "soybean_prices.csv")))
    s = analyze("Soybean", series)
    assert s.n >= 30
    assert s.trend == "up"          # the sample series rises over the period
    assert s.high >= s.latest >= s.low
