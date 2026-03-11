# Travel Agent Tutorial Project

This repository is a tutorial-first scaffold for building a travel planning agent with `DeepSeek`, `AutoNavi (Gaode)`, `MCP`, file-based `Skills`, and a later `LangChain` integration.

The structure now follows the article's engineering path:

- `src/travel_agent/tools`: direct, deterministic travel tools
- `src/travel_agent/tool_registry.py`: exports Python tools as OpenAI/DeepSeek function definitions
- `src/travel_agent/agent/react.py`: an explicit tool-calling ReAct loop
- `src/travel_agent/mcp`: the seam for promoting shared capabilities into an MCP server/client boundary
- `skills/`: file-based skill bundles with `meta.json`, `SKILL.md`, and optional scripts/resources
- `docs/steps`: the coaching materials for each tutorial step

Start with [docs/tutorial_plan.md](/Users/danielwong/Dev/travel_agent/docs/tutorial_plan.md), then follow the steps in order. The flow is: build the raw foundation first, then add Skills and MCP, then decide whether `LangChain` should wrap what you already understand.

## Quickstart

1. Copy `.env.example` to `.env`.
2. Apply for `DEEPSEEK_API_KEY` and `AUTONAVI_API_KEY`, then fill them into `.env`.
3. Install dependencies with `uv sync`.
4. Run `uv run python -m travel_agent.main doctor`.
5. Continue with [docs/steps/step-03-autonavi-tools.md](/Users/danielwong/Dev/travel_agent/docs/steps/step-03-autonavi-tools.md) before wiring the first full agent loop.

## References

- [DeepSeek API Docs](https://api-docs.deepseek.com/)
- [LangChain Docs](https://docs.langchain.com/)
- [Model Context Protocol](https://modelcontextprotocol.io/introduction)
- [AutoNavi Web Service Docs](https://lbs.amap.com/api/webservice/summary/)
