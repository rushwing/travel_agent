from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Skill:
    name: str
    when_to_use: str
    checklist: tuple[str, ...] = field(default_factory=tuple)

    def render(self) -> str:
        checklist = "\n".join(f"- {item}" for item in self.checklist)
        return f"[{self.name}] Use when: {self.when_to_use}\n{checklist}".strip()

