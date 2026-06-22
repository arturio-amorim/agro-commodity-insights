#!/usr/bin/env python
"""Analyze a commodity price series — fully offline, no key.

    python scripts/analyze.py --csv data/soybean_prices.csv --name Soybean
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from agromarket.analyze import analyze  # noqa: E402
from agromarket.data_io import load_csv, prices  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    ap = argparse.ArgumentParser(description="Commodity price analytics.")
    ap.add_argument("--csv", default=str(ROOT / "data" / "soybean_prices.csv"))
    ap.add_argument("--name", default="Soybean")
    args = ap.parse_args()

    series = prices(load_csv(args.csv))
    s = analyze(args.name, series)

    print(f"{s.commodity}  ({s.n} points)")
    print(f"  latest        {s.latest}")
    print(f"  1-period      {s.change_1d_pct:+.2f}%")
    print(f"  ~30-period    {s.change_30d_pct:+.2f}%")
    print(f"  SMA(5)/SMA(20) {s.sma_short} / {s.sma_long}")
    print(f"  volatility    {s.volatility_pct:.2f}%")
    print(f"  trend         {s.trend}")
    print(f"  high / low    {s.high} / {s.low}")


if __name__ == "__main__":
    main()
