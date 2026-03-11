from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class SkillBundle:
    name: str
    description: str
    root: Path
    meta_path: Path
    prompt_path: Path
    scripts_dir: Path


def load_skill_bundles(root: Path | None = None) -> list[SkillBundle]:
    skills_root = root or Path(__file__).resolve().parents[3] / "skills"
    if not skills_root.exists():
        return []

    bundles: list[SkillBundle] = []
    for candidate in sorted(skills_root.iterdir()):
        meta_path = candidate / "meta.json"
        prompt_path = candidate / "SKILL.md"
        if not candidate.is_dir() or not meta_path.exists() or not prompt_path.exists():
            continue
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        bundles.append(
            SkillBundle(
                name=meta["name"],
                description=meta["description"],
                root=candidate,
                meta_path=meta_path,
                prompt_path=prompt_path,
                scripts_dir=candidate / "scripts",
            )
        )
    return bundles
