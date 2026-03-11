# Step 2: Project Setup

## Goal

Make the project runnable with local configuration, a CLI entry point, and a clean dependency workflow.

## Status

Approved.

## Basic knowledge

- The article starts by standardizing Python and package management with `pyenv` and `uv`. The point is not the exact tools; it is reproducibility.
- The model and map APIs are external dependencies, so secrets belong in `.env`, not in code.
- A small CLI makes debugging much easier than starting with a UI.
- A `doctor` command is worth adding early because most failures in agent projects are configuration mistakes.
- For this tutorial, you should obtain both API keys now:
  `DEEPSEEK_API_KEY` for the model and `AUTONAVI_API_KEY` for map/weather data.

## What you will work with

- `pyproject.toml`
- `.env.example`
- `src/travel_agent/config.py`
- `src/travel_agent/app.py`
- `src/travel_agent/main.py`

## What is intentionally stubbed

For Step 2, the following methods are intentionally left for you to implement:

- `Settings.has_llm_credentials`
- `Settings.has_map_credentials`
- `get_settings()`
- `TravelAgentApp.doctor()`
- `main.doctor()`
- `main.run()`

The `ask` CLI command is also stubbed, but that belongs to a later step once the agent loop is ready.

## Suggested implementation order

1. Implement `Settings.has_llm_credentials` and `Settings.has_map_credentials`.
2. Implement `get_settings()` with caching.
3. Implement `TravelAgentApp.doctor()` to return a JSON-serializable report.
4. Implement the `doctor` CLI command.
5. Implement `run()` so `python -m travel_agent.main doctor` works.

## Acceptance check

You should be able to run:

```bash
uv sync
uv run python -m travel_agent.main doctor
```

The command does not need to prove the keys are valid yet. For Step 2, it is enough to prove they are loaded and reported correctly.

## Approved outcome

The current implementation now satisfies Step 2:

- `.env` values are loaded through `Settings`
- `doctor` reports local configuration state without requiring external API calls
- `python -m travel_agent.main doctor` runs successfully
- the `ask` command remains intentionally deferred to a later step

## Guiding question

Can your local environment prove that both `DEEPSEEK_API_KEY` and `AUTONAVI_API_KEY` are wired correctly before you ask the agent to plan a trip?
