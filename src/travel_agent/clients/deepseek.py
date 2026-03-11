from __future__ import annotations

from langchain_openai import ChatOpenAI

from travel_agent.config import Settings


def build_llm(settings: Settings) -> ChatOpenAI:
    if not settings.deepseek_api_key:
        raise ValueError("DEEPSEEK_API_KEY is required before building the agent.")
    return ChatOpenAI(
        model=settings.deepseek_model,
        api_key=settings.deepseek_api_key,
        base_url=settings.deepseek_base_url,
        temperature=0.2,
        timeout=settings.request_timeout_seconds,
    )

