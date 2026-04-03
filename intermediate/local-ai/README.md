# 🏠 Local AI (Ollama) 🔥

## What is this?
Local AI means running large language models (LLMs) on your **own computer** instead of using a cloud service like OpenAI or Anthropic. **Ollama** is the most popular tool for making this easy.

## Why it matters
1.  **Privacy**: Your data never leaves your machine.
2.  **Cost**: You only pay for electricity, not tokens.
3.  **Speed**: No internet delay (if you have a good GPU!).
4.  **Ownership**: You own the model and its outputs.

## How it works (simple)
Think of it like **A Home Garden**.
- **Cloud AI**: A grocery store. You buy what you need, but you don't own the rows of vegetables, and the store knows what you bought.
- **Local AI**: Your own garden. It takes work to set up (you need a good computer), but once it's growing, you can pick whenever you want, and no one sees what's in your basket.

## Example
Interacting with a local model using Python and the Ollama library.

```python
import ollama

# 1. Ask a question to a local model (e.g., Llama 3)
response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])

print(response['message']['content'])
```

## When to use it
- When you are working with sensitive data (e.g., medical, legal, personal).
- When you are a developer testing massive numbers of prompts and want to save money.
- When you want to build an AI that works without an internet connection.

## Related skills
- [What is AI?](../../basics/what-is-ai)
- [private-local-assistant](../../projects/private-local-assistant)

[**← Back to Learning Path**](../../LEARNING_PATH.md)
