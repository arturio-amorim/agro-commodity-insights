#!/usr/bin/env python
"""Analyze a series and generate a narrative market report (needs an API key).

    python scripts/report.py --csv data/soybean_prices.csv --name Soybean
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from agromarket.analyze import analyze  # noqa: E402
from agromarket.config import get_settings  # noqa: E402
from agromarket.data_io import load_csv, prices  # noqa: E402
from agromarket.report import report  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    ap = argparse.ArgumentParser(description="Commodity market report.")
    ap.add_argument("--csv", default=str(ROOT / "data" / "soybean_prices.csv"))
    ap.add_argument("--name", default="Soybean")
    args = ap.parse_args()

    series = prices(load_csv(args.csv))
    summary = analyze(args.name, series)
    print(report(summary, get_settings()))


if __name__ == "__main__":
    main()
