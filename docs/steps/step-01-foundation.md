# Step 1: Foundations

## Goal

Understand the difference between `tools`, `tool registry`, `skills`, `MCP`, and later `LangChain` orchestration before writing more code.

## Basic knowledge

### Tool

A tool does deterministic work. In this project, `AutoNavi` geocoding and weather lookup are tools because they fetch factual data from an API.

### Tool Registry

A registry is the translation layer between your Python code and the model. The article's key point is that you should not hand-maintain a pile of JSON tool definitions if your code already has function signatures, type hints, and docstrings.

### Skill

A skill is a reusable playbook packaged as files. It tells the agent how to think through a domain task and can also carry scripts or resources, for example:

- collect trip constraints first
- ground facts with tools
- compare options explicitly
- produce a travel plan with caveats

### MCP

`MCP` is the boundary for capabilities hosted outside this process. If later you want hotel search, ticketing, or a shared company travel knowledge base, expose those through MCP instead of cramming everything into the main app.

### LangChain

`LangChain` can manage the model-tool loop, but this tutorial uses it after you understand the raw mechanism first. Keep your travel concepts, output schemas, and API wrappers in your own code either way.

## What you should decide now

Pick a narrow first slice. A good first slice is:

- one destination city
- one short time horizon
- one or two trusted tools
- a small output format

Bad first slices:

- full trip booking
- multi-agent planning
- memory-heavy chat
- flight and hotel integration on day one

## Deliverable

Write down the first user story you want this travel agent to solve. Example:

`Plan a weather-aware 2-day weekend trip in Hangzhou for food and walking, grounded with AutoNavi data.`

## Chosen slice

For this tutorial, the chosen slice is:

`Plan a weather-aware 2-day weekend trip in Hangzhou for food and walking, grounded with AutoNavi data.`

## Coaching contract

- You implement the code.
- I provide the concepts, interfaces, and review standard for each step.
- I review your result before we declare the step complete.

## Guiding question

What is your first narrow product slice for this tutorial: a single-city weekend planner, a weather-aware day planner, or a multi-city itinerary planner?
