.PHONY: install test doctor ask

install:
	uv sync

test:
	uv run pytest

doctor:
	uv run python -m travel_agent.main doctor

ask:
	uv run python -m travel_agent.main ask "Plan a weather-aware 2-day trip in Hangzhou"

