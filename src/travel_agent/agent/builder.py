from __future__ import annotations

from collections.abc import Sequence

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from travel_agent.clients.deepseek import build_llm
from travel_agent.config import Settings
from travel_agent.mcp.client import MCPClient
from travel_agent.prompts.system import render_system_prompt
from travel_agent.skills.registry import render_skill_block, resolve_skills
from travel_agent.tools.amap import AutoNaviClient, build_amap_tools


def build_agent(settings: Settings, skill_names: Sequence[str]) -> AgentExecutor:
    selected_skills = resolve_skills(skill_names)
    skill_block = render_skill_block(selected_skills)
    mcp_client = MCPClient(
        enabled=settings.enable_mcp,
        server_url=settings.mcp_server_url,
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", render_system_prompt(skill_block, mcp_client.render_prompt_block())),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    llm = build_llm(settings)
    tools = build_amap_tools(AutoNaviClient(settings))
    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=settings.app_env == "dev")

