from __future__ import annotations

from collections.abc import Iterable, Sequence

from travel_agent.skills.base import Skill


def load_builtin_skills() -> list[Skill]:
    return [
        Skill(
            name="travel_research",
            when_to_use="The user needs a concise travel-planning workflow for a destination.",
            checklist=(
                "Collect trip length, interests, and mobility constraints.",
                "Ground location and weather facts with tools when possible.",
                "Compare at least two candidate activity patterns before deciding.",
            ),
        ),
        Skill(
            name="weather_guardrails",
            when_to_use="Weather can change the feasibility of the itinerary.",
            checklist=(
                "Check weather before suggesting outdoor-heavy plans.",
                "Offer an indoor fallback when the weather is risky.",
            ),
        ),
        Skill(
            name="budget_guardrails",
            when_to_use="The user cares about spend or tradeoffs.",
            checklist=(
                "State where costs can vary by season or neighborhood.",
                "Separate must-have activities from optional splurges.",
            ),
        ),
        Skill(
            name="local_transport",
            when_to_use="The user needs guidance on how to move around the city.",
            checklist=(
                "Prefer realistic district-by-district movement.",
                "Warn when the plan adds too much cross-city travel.",
            ),
        ),
    ]


def resolve_skills(requested_names: Sequence[str]) -> list[Skill]:
    registry = {skill.name: skill for skill in load_builtin_skills()}
    if not requested_names:
        return []

    resolved: list[Skill] = []
    for name in requested_names:
        try:
            resolved.append(registry[name])
        except KeyError as exc:
            raise KeyError(f"Unknown skill '{name}'. Run 'list-skills' to inspect choices.") from exc
    return resolved


def render_skill_block(skills: Iterable[Skill]) -> str:
    rendered = [skill.render() for skill in skills]
    if not rendered:
        return "No optional skills are enabled for this run."
    return "\n\n".join(rendered)

