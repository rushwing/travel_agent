# Future Challenges

Use this file as the place to append stretch work after you complete each step correctly.

## Seeded backlog

- Add a real `ToolRegistry.register_from_class()` introspection flow so docstrings and type hints fully drive schema generation.
- Split the direct ReAct loop into traceable planner/executor components once the single-loop version is stable.
- Refactor the agent loop to `LangGraph` once the direct LangChain agent works reliably.
- Add a cached place-lookup layer so repeated AutoNavi calls do not waste quota.
- Add a budget-estimation skill with explicit currency assumptions.
- Add hotel, train, or flight search through a dedicated MCP server instead of hardcoding more HTTP tools.
- Introduce structured itinerary output validation with `pydantic` and retry-on-parse-failure.
- Build a small evaluation set of real travel questions from your own trips and run regression checks.
- Add conversation memory only after single-turn behavior is stable.
- Add a simple web or chat UI after the CLI workflow is stable.
