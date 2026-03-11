# Step 7: LangChain Adapter, Evaluation, and Hardening

## Goal

Add a LangChain wrapper only after the raw loop is clear, then add tests and lightweight evaluation so the project stays understandable as it grows.

## Basic knowledge

- `LangChain` is useful when it reduces boilerplate, not when it hides concepts you do not yet understand.
- Agent regressions often come from prompt drift and tool-description drift, not only code changes.
- Start with a tiny evaluation set based on realistic user questions.
- Track failures in `docs/lessons_learned.md` instead of relying on memory.

## Acceptance check

You should have:

- one working manual loop
- one optional LangChain adapter over the same tools
- unit tests for configuration and skill resolution
- a few representative prompts saved as regression cases
- a short list of common failure modes

## Guiding question

What does LangChain simplify in your project today, and what would become harder to debug if you adopted it too early?
