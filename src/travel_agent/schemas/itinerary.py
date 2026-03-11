from __future__ import annotations

from pydantic import BaseModel, Field


class DayPlan(BaseModel):
    day: int = Field(..., ge=1)
    theme: str
    morning: str
    afternoon: str
    evening: str
    notes: list[str] = Field(default_factory=list)


class TravelPlan(BaseModel):
    city: str
    duration_days: int = Field(..., ge=1)
    summary: str
    weather_notes: list[str] = Field(default_factory=list)
    days: list[DayPlan] = Field(default_factory=list)

