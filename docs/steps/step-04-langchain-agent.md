# Step 4: Tool Registry and ReAct Loop

## Goal

Create the first raw agent loop that can call tools through `DeepSeek`, using a registry instead of hardcoded tool JSON.

## Basic knowledge

- The article's core engineering move is `write Python tools -> register them -> export schemas -> run the loop`.
- A `ToolRegistry` should own schema export and tool execution so the ReAct loop stays small.
- Use the model for reasoning and tool selection, not as the source of truth for live map data.
- Keep the first loop single-purpose. Complexity grows faster than expected.

## Acceptance check

Ask the raw agent a question like:

`Plan a 2-day trip in Suzhou and check the weather before proposing outdoor activities.`

The agent should export the tools, receive a `tool_calls` response, execute the weather tool, append the result as a `tool` message, and only then commit to the plan.

## Guiding question

How will you inspect the loop to prove that the model really emitted `tool_calls` and did not answer from memory instead?
