from travel_agent.config import Settings


def test_default_service_urls(monkeypatch) -> None:
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    monkeypatch.delenv("AUTONAVI_API_KEY", raising=False)
    settings = Settings()
    assert settings.deepseek_base_url == "https://api.deepseek.com"
    assert settings.autonavi_base_url == "https://restapi.amap.com"
    assert settings.has_llm_credentials is False
    assert settings.has_map_credentials is False


def test_credential_flags(monkeypatch) -> None:
    monkeypatch.setenv("DEEPSEEK_API_KEY", "demo-llm-key")
    monkeypatch.setenv("AUTONAVI_API_KEY", "demo-map-key")
    settings = Settings()
    assert settings.has_llm_credentials is True
    assert settings.has_map_credentials is True

