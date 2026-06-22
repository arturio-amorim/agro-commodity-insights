"""Load price series from CSV (date,price)."""
from __future__ import annotations

import csv
from typing import List

from .models import PricePoint


def load_csv(path: str) -> List[PricePoint]:
    points: List[PricePoint] = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            points.append(PricePoint(date=row["date"], price=float(row["price"])))
    if not points:
        raise ValueError(f"no rows found in {path!r}")
    return points


def prices(points: List[PricePoint]) -> List[float]:
    return [p.price for p in points]
