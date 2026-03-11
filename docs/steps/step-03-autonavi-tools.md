# Step 3: AutoNavi Tools

## Goal

Wrap `AutoNavi` as deterministic tools before asking the LLM to plan anything.

## Basic knowledge

- A grounded agent should fetch map facts from tools, not from model memory.
- Keep tool inputs narrow and explicit.
- Tool descriptions and docstrings matter because they are part of the agent policy surface and later feed the registry schema.

## Starter tool set

- `amap_geocode_address`
- `amap_reverse_geocode`
- `amap_weather`
- later: `search_poi`
- later: `route_planning`
- later: `estimate_travel_cost`

## Acceptance check

Each tool should:

- fail loudly when the API key is missing
- surface AutoNavi error payloads clearly
- return a compact structured summary that the model can use

## Guiding question

Which travel facts in your first product slice must always come from AutoNavi tools rather than the model's prior knowledge?
