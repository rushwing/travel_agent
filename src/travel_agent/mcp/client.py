from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MCPClient:
    enabled: bool
    server_url: str | None = None

    def render_prompt_block(self) -> str:
        if not self.enabled:
            return "MCP is disabled. Use only local tools and skills."
        if not self.server_url:
            return (
                "MCP is enabled but no server URL is configured. Do not assume external MCP "
                "capabilities exist yet."
            )
        return (
            "MCP is enabled. Ask the MCP adapter for additional capabilities from "
            f"{self.server_url} once Step 6 is implemented."
        )

