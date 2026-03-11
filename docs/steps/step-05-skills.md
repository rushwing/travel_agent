# Step 5: Skills Layer

## Goal

Package travel-planning know-how into reusable filesystem skills instead of growing one prompt forever.

## Basic knowledge

- The article uses the `meta -> SKILL.md -> scripts/resources` structure.
- Skills are best when they capture a repeatable workflow, not a random paragraph of advice.
- Progressive disclosure matters: always load metadata, load `SKILL.md` on match, and load scripts/resources only when needed.
- Skill routing can itself be implemented through model tool selection by treating skill metadata as callable route markers.

## Seed skills

- `weekend_city_planner`
- `weather_guardrails`
- `budget_guardrails`
- `local_transport`

## Acceptance check

You should be able to route into one skill via metadata, inject the selected `SKILL.md`, and compare the output with and without that skill context.

## Guiding question

Which planning behavior should become a reusable skill because you expect to use it across many travel questions?
