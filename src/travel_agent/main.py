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
    """Step 2 wire the doctor command to the application health report."""
    travel_app = TravelAgentApp()
    results = travel_app.doctor()
    for name, value in results.items():
        print(f"TravelApp ready check -> {name}: {value}.")


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
    """Future step: invoke the travel agent once the tool loop is implemented."""
    raise NotImplementedError(
        "Future step: implement the ask CLI command after the agent loop is ready."
    )


def run() -> None:
    """Step 2 expose the Typer application as the CLI entry point."""
    app()


if __name__ == "__main__":
    run()
