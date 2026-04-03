# 🕵️ AI Agents: Machines that Act

## What is this?
An AI Agent is a "brain" (LLM) that is given **tools** (like a calculator, a web browser, or a database) and a **goal**. Instead of just talking, the agent can **take actions** to achieve its goal.

## Why it matters
Normal AI is just a chatbot; it can tell you how to bake a cake, but it can't order the ingredients for you. An **Agent** can log into your grocery app, buy the flour, and tell you when it's arriving.

## How it works (simple)
Think of an Agent like a **Personal Assistant**.
- **The Chatbot**: You ask "What's the weather?" and it says "It usually rains in April."
- **The Agent**: You ask "What's the weather?" and it:
    1.  **Thinks**: "I need to check the current weather."
    2.  **Acts**: Opens a weather website.
    3.  **Observes**: Sees it's 75°F and sunny.
    4.  **Concludes**: Tells you "It's 75°F and sunny right now!"

This loop is called **ReAct** (Reason + Act).

## Example
Here is a conceptual ReAct loop in Python.

```python
def calculator_tool(expression):
    return eval(expression) # A simple tool

def agent_loop(task):
    print(f"Goal: {task}")
    
    # 1. Thought
    print("THOUGHT: I need to calculate 15% of 200.")
    
    # 2. Action
    result = calculator_tool("0.15 * 200")
    print(f"ACTION: Used calculator. Result = {result}")
    
    # 3. Final Answer
    print(f"FINAL ANSWER: 15% of 200 is {result}.")

agent_loop("Calculate my tip for a $200 dinner.")
```

## When to use it
- When you want AI to browse the web for real-time info.
- When you want AI to write and execute code.
- When you want AI to manage complex workflows (e.g., "Research this topic and write a report").

## Related skills
- [Multi-Agent Systems](../multi-agent-systems)
- [Prompt Engineering](../../basics/prompt-engineering)

[**← Back to Learning Path**](../../LEARNING_PATH.md)
