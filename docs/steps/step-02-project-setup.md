# Step 2: Project Setup

## Goal

Make the project runnable with local configuration, a CLI entry point, and a clean dependency workflow.

## Basic knowledge

- The article starts by standardizing Python and package management with `pyenv` and `uv`. The point is not the exact tools; it is reproducibility.
- The model and map APIs are external dependencies, so secrets belong in `.env`, not in code.
- A small CLI makes debugging much easier than starting with a UI.
- A `doctor` command is worth adding early because most failures in agent projects are configuration mistakes.

## What you will work with

- `pyproject.toml`
- `.env.example`
- `src/travel_agent/config.py`
- `src/travel_agent/main.py`

## Acceptance check

You should be able to run:

```bash
uv sync
uv run python -m travel_agent.main doctor
```

## Guiding question

Can your local environment prove that both `DEEPSEEK_API_KEY` and `AUTONAVI_API_KEY` are wired correctly before you ask the agent to plan a trip?
