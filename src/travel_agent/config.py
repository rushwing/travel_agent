from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "dev"
    deepseek_api_key: str = ""
    deepseek_base_url: str = "https://api.deepseek.com"
    deepseek_model: str = "deepseek-chat"
    autonavi_api_key: str = ""
    autonavi_base_url: str = "https://restapi.amap.com"
    enable_mcp: bool = False
    mcp_server_url: str | None = None
    request_timeout_seconds: float = Field(default=20.0, gt=0)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def has_llm_credentials(self) -> bool:
        """Step 2 report whether the DeepSeek credential is configured."""
        return bool(self.deepseek_api_key)

    @property
    def has_map_credentials(self) -> bool:
        """Step 2 report whether the AutoNavi credential is configured."""
        return bool(self.autonavi_api_key)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Step 2 construct and cache the application settings object."""
    settings = Settings()
    return settings
