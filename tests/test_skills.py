import pytest

from travel_agent.skills.registry import load_builtin_skills, render_skill_block, resolve_skills


def test_builtin_skills_exist() -> None:
    skills = load_builtin_skills()
    names = {skill.name for skill in skills}
    assert "travel_research" in names
    assert "weather_guardrails" in names


def test_render_skill_block() -> None:
    block = render_skill_block(resolve_skills(["budget_guardrails"]))
    assert "budget_guardrails" in block
    assert "costs can vary" in block


def test_unknown_skill_raises() -> None:
    with pytest.raises(KeyError):
        resolve_skills(["missing_skill"])
