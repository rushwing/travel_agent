from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from travel_agent.agent.builder import build_agent
from travel_agent.config import Settings, get_settings


class TravelAgentApp:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()

    def ask(self, question: str, skill_names: Sequence[str] | None = None) -> dict[str, Any]:
        executor = build_agent(self.settings, skill_names=skill_names or [])
        return executor.invoke({"input": question})

    def doctor(self) -> dict[str, bool | str | None]:
        return {
            "app_env": self.settings.app_env,
            "deepseek_model": self.settings.deepseek_model,
            "deepseek_base_url": self.settings.deepseek_base_url,
            "autonavi_base_url": self.settings.autonavi_base_url,
            "deepseek_api_key_configured": self.settings.has_llm_credentials,
            "autonavi_api_key_configured": self.settings.has_map_credentials,
            "mcp_enabled": self.settings.enable_mcp,
            "mcp_server_url": self.settings.mcp_server_url,
        }

