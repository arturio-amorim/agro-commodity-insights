"""Configuration for the (optional) LLM market report."""
from __future__ import annotations

import os
from dataclasses import dataclass

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:  # pragma: no cover
    pass


@dataclass
class Settings:
    llm_provider: str = os.getenv("LLM_PROVIDER", "anthropic")
    gen_model: str = os.getenv("GEN_MODEL", "claude-sonnet-4-6")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    @property
    def model(self) -> str:
        return self.gen_model if self.llm_provider == "anthropic" else self.openai_model


def get_settings() -> Settings:
    return Settings()
