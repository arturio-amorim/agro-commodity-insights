"""agromarket — agricultural commodity price analytics + LLM market report.

Indicators and analysis are pure-Python (no pandas/numpy) and fully tested;
only the narrative report calls an LLM.
"""
from .analyze import analyze
from .config import Settings, get_settings
from .models import MarketSummary, PricePoint

__version__ = "0.1.0"
__all__ = ["analyze", "Settings", "get_settings", "MarketSummary", "PricePoint", "__version__"]
