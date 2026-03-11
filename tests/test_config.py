from travel_agent.config import Settings


def test_default_service_urls(monkeypatch) -> None:
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    monkeypatch.delenv("AUTONAVI_API_KEY", raising=False)
    settings = Settings()
    assert settings.deepseek_base_url == "https://api.deepseek.com"
    assert settings.autonavi_base_url == "https://restapi.amap.com"


def test_settings_read_env_values(monkeypatch) -> None:
    monkeypatch.setenv("DEEPSEEK_API_KEY", "demo-llm-key")
    monkeypatch.setenv("AUTONAVI_API_KEY", "demo-map-key")
    settings = Settings()
    assert settings.deepseek_api_key == "demo-llm-key"
    assert settings.autonavi_api_key == "demo-map-key"
