from __future__ import annotations

from typing import Any

from openai import AsyncOpenAI

from travel_agent.config import Settings
from travel_agent.tool_registry import ToolRegistry


class ReactToolAgent:
    def __init__(
        self,
        settings: Settings,
        *,
        system_prompt: str,
        tool_registry: ToolRegistry,
        max_iterations: int = 8,
    ) -> None:
        self.settings = settings
        self.system_prompt = system_prompt
        self.tool_registry = tool_registry
        self.max_iterations = max_iterations
        self.client = AsyncOpenAI(
            api_key=settings.deepseek_api_key,
            base_url=settings.deepseek_base_url,
        )

    async def run(self, user_input: str) -> str:
        messages: list[dict[str, Any]] = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_input},
        ]

        for _ in range(self.max_iterations):
            result = await self.client.chat.completions.create(
                model=self.settings.deepseek_model,
                messages=messages,
                tools=self.tool_registry.export_openai_tools(),
            )
            assistant_message = result.choices[0].message
            content = assistant_message.content or ""

            if not assistant_message.tool_calls:
                return content

            tool_calls = [
                {
                    "id": call.id,
                    "type": call.type,
                    "function": {
                        "name": call.function.name,
                        "arguments": call.function.arguments,
                    },
                }
                for call in assistant_message.tool_calls
            ]
            messages.append(
                {
                    "role": "assistant",
                    "content": content,
                    "tool_calls": tool_calls,
                }
            )

            for tool_call in assistant_message.tool_calls:
                tool_result = await self.tool_registry.execute_tool(
                    tool_call.function.name,
                    tool_call.function.arguments,
                )
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_result,
                    }
                )

        raise RuntimeError("The ReAct loop reached the iteration limit without a final answer.")

