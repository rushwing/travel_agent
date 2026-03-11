from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from travel_agent.config import Settings, get_settings


class TravelAgentApp:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()

    def ask(self, question: str, skill_names: Sequence[str] | None = None) -> dict[str, Any]:
        from travel_agent.agent.builder import build_agent
        executor = build_agent(self.settings, skill_names=skill_names or [])
        return executor.invoke({"input": question})

    def doctor(self) -> dict[str, bool | str]:
        """Step 2 return a serializable configuration health report."""
        results = self.AppDoctor(self.settings).run_all()
        all_passed = all(v is True for v in results.values())
        if all_passed:
            print("🎉 所有检查已通过！应用可以正常启动。")
        else:
            print("⚠️ 诊断发现问题，请修复上述错误后再试。")
        return results

    class AppDoctor:
        def __init__(self, settings: Settings) -> None:
            self.settings = settings

        def _report(self, name: str, passed: bool, message: str) -> tuple[str, bool | str]:
            return name, True if passed else f"❌ {name}: {message}"

        def check_llm_key(self) -> tuple[str, bool | str]:
            if not self.settings.has_llm_credentials:
                return self._report("LLM Key", False, "DEEPSEEK_API_KEY not configured")
            # TODO Step 4+: make a minimal API call to validate the key
            return self._report("LLM Key", True, "")

        def check_amap_key(self) -> tuple[str, bool | str]:
            if not self.settings.has_map_credentials:
                return self._report("AutoNavi", False, "AUTONAVI_API_KEY not configured")
            # TODO Step 3+: make a minimal geocode request to validate the key
            return self._report("AutoNavi", True, "")

        def check_mcp_servers(self) -> tuple[str, bool | str]:
            if not self.settings.enable_mcp:
                return self._report("MCP Server", True, "")
            if not self.settings.mcp_server_url:
                return self._report("MCP Server", False, "MCP_SERVER_URL not provided")
            # TODO Step 6+: verify MCP server connectivity
            return self._report("MCP Server", True, "")

        def run_all(self) -> dict[str, bool | str]:
            checks = [
                self.check_llm_key(),
                self.check_amap_key(),
                self.check_mcp_servers(),
            ]
            return {name: result for name, result in checks}
