# Lessons Learned

Use this file to capture problems you hit during the tutorial and the fix that resolved them. The starter entries below cover the most common failure modes in this stack.

## Sample: Hatch cannot build the package

- Symptom: `uv run pytest` fails before tests run and reports that Hatch cannot determine which files to ship.
- Likely cause: the project name differs from the import package name, but `tool.hatch.build.targets.wheel.packages` is not configured.
- Fix: set `packages = ["src/travel_agent"]` in `pyproject.toml`.

## Sample: DeepSeek authentication fails

- Symptom: requests to the model return `401` or `invalid_api_key`.
- Likely cause: `DEEPSEEK_API_KEY` is missing or points at the wrong base URL.
- Fix: confirm `.env`, then run `uv run python -m travel_agent.main doctor` and make sure the CLI reports that the model key is configured.

## Sample: AutoNavi rejects the request

- Symptom: tool output contains `INVALID_USER_KEY`, `DAILY_QUERY_OVER_LIMIT`, or a status of `0`.
- Likely cause: the key is wrong, the quota is exhausted, or the API product is not enabled.
- Fix: check the key in the AutoNavi console, confirm the related Web Service API is enabled, and reduce retry loops while testing.

## Sample: The agent answers from memory instead of calling tools

- Symptom: the response guesses weather or coordinates without using AutoNavi.
- Likely cause: tool descriptions are weak, the registry exports vague schemas, or the system prompt does not require tool use for factual map data.
- Fix: tighten the tool descriptions, inspect the exported tool schema, and require tool use for location, weather, route, and map facts when available.

## Sample: MCP is enabled but nothing new appears

- Symptom: turning on `ENABLE_MCP=true` changes nothing.
- Likely cause: the scaffold only exposes the seam; you still need an actual MCP server and a loader that converts capabilities into tools.
- Fix: finish Step 6 and point `MCP_SERVER_URL` at a real server that lists travel-related tools.

## Template

### Lesson title

- Symptom:
- Root cause:
- Fix:
- Prevention:
