# 🏗️ Context Engineering 🔥

## What is this?
Context Engineering is the evolution of "Prompt Engineering." Instead of just writing a good instruction, you are **designing the entire environment** in which the AI works. This includes structured data, system instructions, and few-shot examples.

## Why it matters
In production software, a "lucky" prompt isn't enough. You need the AI to produce the **exact same format** every single time. Context Engineering ensures the AI behaves predictably, like a traditional piece of code.

## How it works (simple)
Think of it like **Building a specialized workshop**.
- **Prompt Engineering**: Giving a carpenter a sticky note that says "Make me a chair."
- **Context Engineering**: Putting the carpenter in a workshop that only has chair parts, a chair manual on the wall, and a sign that says "Only use these tools."

## Example
**Loose Prompt (Old way):**
"Tell me the price of this product from the text below."

**Structured Context (Context Engineering):**
```text
SYSTEM: You are a data extraction engine. 
ROLE: Extract the 'price' field from the user's text.
FORMAT: Return ONLY a JSON object: {"price": float, "currency": string}.
EXAMPLES:
Input: "The shoes cost 59.99 dollars." -> Output: {"price": 59.99, "currency": "USD"}
Input: "Price: 10€" -> Output: {"price": 10.0, "currency": "EUR"}
```

## When to use it
- When your AI is connected to a database or API.
- When you need consistent JSON or code outputs.
- When you are building high-stakes applications (e.g., medical or financial data).

## Related skills
- [Prompt Engineering](../prompt-engineering)
- [smolagents](../../tools/smolagents)

[**← Back to Learning Path**](../../LEARNING_PATH.md)
