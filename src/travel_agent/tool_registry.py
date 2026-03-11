from __future__ import annotations

from dataclasses import dataclass
import inspect
import json
from typing import Any

from pydantic import BaseModel


@dataclass(frozen=True)
class RegisteredTool:
    name: str
    description: str
    parameters: dict[str, Any]
    args_schema: type[BaseModel]
    function: Any

    def to_openai_tool(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters,
            },
        }


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, RegisteredTool] = {}

    def register_function(
        self,
        func: Any,
        *,
        args_schema: type[BaseModel],
        name: str | None = None,
        description: str | None = None,
    ) -> None:
        tool_name = name or func.__name__
        tool_description = description or inspect.getdoc(func) or f"Call {tool_name}."
        self._tools[tool_name] = RegisteredTool(
            name=tool_name,
            description=tool_description,
            parameters=args_schema.model_json_schema(),
            args_schema=args_schema,
            function=func,
        )

    def export_openai_tools(self) -> list[dict[str, Any]]:
        return [tool.to_openai_tool() for tool in self._tools.values()]

    async def execute_tool(self, name: str, arguments: str | dict[str, Any]) -> str:
        tool = self._tools[name]
        payload = json.loads(arguments) if isinstance(arguments, str) else arguments
        validated = tool.args_schema.model_validate(payload)
        result = tool.function(**validated.model_dump())
        if inspect.isawaitable(result):
            result = await result
        if isinstance(result, str):
            return result
        return json.dumps(result, ensure_ascii=True, indent=2)

