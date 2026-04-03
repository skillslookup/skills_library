# 🤖 What is AI?

## What is this?
Artificial Intelligence (AI) is the ability of a computer program or a machine to **think and learn**. It is also a field of study which tries to make computers "smart" enough to solve problems usually done by humans.

## Why it matters
AI is everywhere! From the recommendations you get on Netflix to the way doctors diagnose diseases, AI helps humans process massive amounts of information faster and more accurately than ever before.

## How it works (simple)
Think of AI like a **Super Librarian**. 
- A normal librarian knows where the books are.
- A Super Librarian has read **every single book in the world**. 
- When you ask a question, they don't just point to a book; they **summarize** the answer for you based on everything they've ever read.

## Example
Here is a simple example of how an AI "thinks" about a sentence. Instead of just seeing words, it sees **patterns**.

```python
# A simple representation of how AI might 'predict' the next word.
# It doesn't 'know' English; it knows what usually comes next.

sentence_start = "The weather is very"
predictions = {
    "sunny": 0.85,  # 85% chance
    "cold": 0.10,   # 10% chance
    "purple": 0.01  # 1% chance (unlikely!)
}

print(f"Start: {sentence_start}")
print(f"Top Prediction: {max(predictions, key=predictions.get)}")
```

## When to use it
- When you have a lot of data and need to find patterns.
- When you need a computer to make predictions about the future.
- When you want to automate repetitive tasks that require some "common sense."

## Related skills
- [How LLMs Work](../how-llms-work)
- [Prompt Engineering](../prompt-engineering)

[**← Back to Learning Path**](../../LEARNING_PATH.md)
