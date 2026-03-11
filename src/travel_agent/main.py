from __future__ import annotations

from collections.abc import Sequence
import json

import typer

from travel_agent.app import TravelAgentApp
from travel_agent.skills.filesystem import load_skill_bundles
from travel_agent.skills.registry import load_builtin_skills

app = typer.Typer(help="CLI for the DeepSeek + AutoNavi travel agent tutorial.")


def _parse_skills(skills: str) -> Sequence[str]:
    if not skills.strip():
        return []
    return [name.strip() for name in skills.split(",") if name.strip()]


@app.command()
def doctor() -> None:
    """Print configuration status without making external calls."""
    report = TravelAgentApp().doctor()
    typer.echo(json.dumps(report, indent=2, sort_keys=True))


@app.command()
def list_skills() -> None:
    """Show the built-in tutorial skills."""
    payload = [
        {
            "name": skill.name,
            "when_to_use": skill.when_to_use,
        }
        for skill in load_builtin_skills()
    ]
    typer.echo(json.dumps(payload, indent=2))


@app.command()
def list_skill_bundles() -> None:
    """Show file-based skills discovered from the workspace."""
    payload = [
        {
            "name": bundle.name,
            "description": bundle.description,
            "path": str(bundle.root),
        }
        for bundle in load_skill_bundles()
    ]
    typer.echo(json.dumps(payload, indent=2))


@app.command()
def ask(question: str, skills: str = "") -> None:
    """Ask the travel agent a single question."""
    result = TravelAgentApp().ask(question, skill_names=_parse_skills(skills))
    typer.echo(result["output"])


def run() -> None:
    app()


if __name__ == "__main__":
    run()
