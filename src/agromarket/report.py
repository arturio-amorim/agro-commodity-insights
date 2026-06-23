"""Generate a narrative market report from indicators (needs an API key)."""
from __future__ import annotations

from .config import Settings
from .models import MarketSummary

SYSTEM_PROMPT = (
    "You are an agricultural commodity market analyst. Write a concise, factual "
    "market note based ONLY on the provided indicators. Do not invent prices, "
    "news, or forecasts beyond what the numbers imply. 3-5 sentences."
)


def report(summary: MarketSummary, settings: Settings) -> str:
    s = summary
    facts = (
        f"Commodity: {s.commodity}\n"
        f"Data points: {s.n}\n"
        f"Latest price: {s.latest}\n"
        f"1-period change: {s.change_1d_pct}%\n"
        f"~30-period change: {s.change_30d_pct}%\n"
        f"SMA(5): {s.sma_short}\n"
        f"SMA(20): {s.sma_long}\n"
        f"Volatility (return stddev): {s.volatility_pct}%\n"
        f"Trend: {s.trend}\n"
        f"Period high: {s.high}\n"
        f"Period low: {s.low}"
    )
    prompt = (
        f"Indicators:\n{facts}\n\n"
        "Write a short market note covering trend, momentum, volatility, and key levels."
    )
    return _call(prompt, settings)


def _call(prompt: str, settings: Settings) -> str:
    if settings.llm_provider == "anthropic":
        import anthropic

        client = anthropic.Anthropic()
        msg = client.messages.create(
            model=settings.gen_model,
            max_tokens=400,
            temperature=0.3,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        )
        return "".join(b.text for b in msg.content if b.type == "text").strip()

    from openai import OpenAI

    if settings.llm_provider == "ollama":
        client = OpenAI(base_url=settings.ollama_base_url, api_key="ollama")  # local, free
        model = settings.ollama_model
    else:
        client = OpenAI()
        model = settings.openai_model
    resp = client.chat.completions.create(
        model=model,
        temperature=0.3,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    return (resp.choices[0].message.content or "").strip()
