from __future__ import annotations

import json

import requests
from langchain_core.tools import BaseTool, StructuredTool
from pydantic import BaseModel, Field

from travel_agent.config import Settings


class GeocodeInput(BaseModel):
    address: str = Field(..., description="Address, district, or place name to geocode.")
    city: str = Field(default="", description="Optional city name to narrow the search.")


class ReverseGeocodeInput(BaseModel):
    longitude: float = Field(..., description="Longitude in decimal degrees.")
    latitude: float = Field(..., description="Latitude in decimal degrees.")


class WeatherInput(BaseModel):
    city: str = Field(
        ...,
        description="City name, citycode, or adcode accepted by AutoNavi weather lookup.",
    )


class AutoNaviClient:
    def __init__(self, settings: Settings) -> None:
        self.base_url = settings.autonavi_base_url.rstrip("/")
        self.api_key = settings.autonavi_api_key
        self.timeout = settings.request_timeout_seconds
        self.session = requests.Session()

    def geocode(self, address: str, city: str = "") -> str:
        payload = self._get(
            "/v3/geocode/geo",
            params={"address": address, "city": city},
        )
        geocodes = payload.get("geocodes", [])
        summary = {
            "query": {"address": address, "city": city},
            "count": len(geocodes),
            "results": geocodes[:3],
        }
        return json.dumps(summary, indent=2, ensure_ascii=True)

    def reverse_geocode(self, longitude: float, latitude: float) -> str:
        payload = self._get(
            "/v3/geocode/regeo",
            params={"location": f"{longitude},{latitude}", "extensions": "base"},
        )
        summary = {
            "query": {"longitude": longitude, "latitude": latitude},
            "result": payload.get("regeocode", {}),
        }
        return json.dumps(summary, indent=2, ensure_ascii=True)

    def weather(self, city: str) -> str:
        payload = self._get(
            "/v3/weather/weatherInfo",
            params={"city": city, "extensions": "all"},
        )
        summary = {
            "query": {"city": city},
            "lives": payload.get("lives", []),
            "forecasts": payload.get("forecasts", []),
        }
        return json.dumps(summary, indent=2, ensure_ascii=True)

    def _get(self, path: str, params: dict[str, str]) -> dict:
        if not self.api_key:
            raise RuntimeError("AUTONAVI_API_KEY is required before using AutoNavi tools.")

        response = self.session.get(
            f"{self.base_url}{path}",
            params={**params, "key": self.api_key},
            timeout=self.timeout,
        )
        response.raise_for_status()
        payload = response.json()
        if payload.get("status") != "1":
            info = payload.get("info", "unknown_error")
            infocode = payload.get("infocode", "unknown_code")
            raise RuntimeError(f"AutoNavi API error: {info} ({infocode})")
        return payload


def build_amap_tools(client: AutoNaviClient) -> list[BaseTool]:
    def geocode_address(address: str, city: str = "") -> str:
        """Look up coordinates and district metadata for an address or place name."""
        return client.geocode(address=address, city=city)

    def reverse_geocode(longitude: float, latitude: float) -> str:
        """Resolve a coordinate pair into a human-readable address and nearby metadata."""
        return client.reverse_geocode(longitude=longitude, latitude=latitude)

    def get_weather(city: str) -> str:
        """Fetch current and forecast weather details for a city or adcode."""
        return client.weather(city=city)

    return [
        StructuredTool.from_function(
            func=geocode_address,
            name="amap_geocode_address",
            description="Use AutoNavi geocoding for factual address-to-coordinate lookup.",
            args_schema=GeocodeInput,
        ),
        StructuredTool.from_function(
            func=reverse_geocode,
            name="amap_reverse_geocode",
            description="Use AutoNavi reverse geocoding for factual coordinate-to-address lookup.",
            args_schema=ReverseGeocodeInput,
        ),
        StructuredTool.from_function(
            func=get_weather,
            name="amap_weather",
            description="Use AutoNavi weather data for grounded current and forecast conditions.",
            args_schema=WeatherInput,
        ),
    ]

