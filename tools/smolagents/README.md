# 🧬 smolagents (Hugging Face) 🔥

## What is this?
**smolagents** is a lightweight library from Hugging Face designed for building AI agents that can **write and run real code** to solve problems. Unlike heavier frameworks, it's focused on simplicity, speed, and reliability.

## Why it matters
1.  **Code-Centric**: It uses a "Code-Interpreter" approach, let the AI write Python to perform actions.
2.  **Fast**: Very low overhead, making it ideal for real-time applications.
3.  **Hugging Face Integration**: Easily switch between models like Llama, DeepSeek, and Claude.

## How it works (simple)
Think of smolagents like **A Smart Calculator**.
- **Normal LLM**: Tries to guess the answer to "What's the square root of 19,481?"
- **smolagents**: Writes a Python script `import math; print(math.sqrt(19481))` and runs it to give you the exact answer.

## Example: A Simple smolagent
```python
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

# 1. Choose a model.
model = HfApiModel()

# 2. Give the agent a tool (like Search).
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

# 3. Task it!
agent.run("How many people live in Paris?")
```

## When to use it
- When you want your AI to perform data analysis or math tasks.
- When you want to build an agent that is "smol" (lightweight) and easy to deploy.
- When you prefer your AI to **show its work** by writing code.

## Related skills
- [Agents](../../advanced/agents)
- [Local AI](../../intermediate/local-ai)

[**← Back to Learning Path**](../../LEARNING_PATH.md)
