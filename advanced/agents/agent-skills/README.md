# 🛡️ Agent-Skills (Anthropic Architecture)

## What is this?
An **Agent Skill** is a modular bundle of instructions, tools, and examples that an AI Agent can load when it needs to perform a specific task. Anthropic uses this pattern to give Claude specialized abilities like "Data Analysis" or "Research."

## Why it matters
Instead of one giant, messy prompt that tries to explain everything, you create a dedicated **SKILL.md** file for each task. This makes your agent more **reliable**, **maintainable**, and **testable**.

## How it works (simple)
Think of it like **A Toolbelt**.
- **The Agent**: The worker.
- **The Skill**: A specialized tool in their belt (e.g., a "Plumbing Kit"). 
When the worker sees a leaky pipe, they open the "Plumbing Kit" which has its own manual and specific tools inside it.

## The SKILL.md Format
A typical skill file contains:
1.  **Metadata**: Name, version, and when to use it.
2.  **Instructions**: How the agent must behave while using this skill.
3.  **Tools**: A list of external functions the agent can call.

## Example: Web Search Skill
[**Check out the web-search-skill/SKILL.md**](./web-search-skill/SKILL.md)

## When to use it
- When you want your agent to have "Modes" (e.g., "Developer Mode", "Researcher Mode").
- When you are building enterprise-grade agents with many complex tools.
- When you want to share AI behaviors with other developers.

## Related skills
- [Agents](../agents)
- [smolagents](../../tools/smolagents)

[**← Back to Learning Path**](../../LEARNING_PATH.md)
