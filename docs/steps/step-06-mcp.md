# Step 6: MCP Integration

## Goal

Add an extension seam for external capabilities that should not live directly inside this repo.

## Basic knowledge

- `MCP` standardizes how tools and resources are exposed across clients.
- The article's distinction is simple: `Tools` are function-level capabilities; `MCP` is the service/protocol layer for longer-lived, shared capabilities.
- Not every tool needs MCP. Start local first, then promote shared capabilities to MCP when reuse justifies the extra boundary.
- Good MCP candidates are hotel search, train data, company travel policy, or a shared place database.

## Acceptance check

Your local app should be able to:

- detect whether MCP is enabled
- fetch and summarize remote MCP tools
- leave room to translate server capabilities into your raw loop and later into LangChain tools

## Guiding question

Which future travel capability would you expose through MCP first, and why is it better there than as another direct HTTP helper in this repo?
