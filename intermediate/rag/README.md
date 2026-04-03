# 📚 RAG: Retrieval Augmented Generation

## What is this?
RAG is a way to give AI "new" or "private" information without retraining the entire model. It allows the AI to **look up** documents from a database before answering your question.

## Why it matters
LLMs (like ChatGPT or Gemini) have a "knowledge cutoff." They don't know about events that happened yesterday or your private company documents. RAG solves this by letting the AI search your specific files to find the right answer.

## How it works (simple)
Think of RAG like an **Open-Book Exam**.
- **Normal AI**: You ask it a question from memory. If it forgets, it might "hallucinate" (make something up).
- **RAG AI**: You give the AI a textbook. Before it answers, it **flips through the pages**, finds the exact paragraph it needs, and **then** writes the answer based on that paragraph.

## Example
Here is a simplified "Open-Book" simulation in Python.

```python
# The 'Textbook' (Our Private Data)
private_data = {
    "Project Blue": "A secret initiative to build a space station on Mars by 2030."
}

def rag_simulation(query):
    # 1. RETRIEVE information (The 'R' in RAG)
    print(f"🔍 Searching for: {query}...")
    knowledge = private_data.get("Project Blue", "No info found.")
    
    # 2. AUGMENT the prompt (The 'A' in RAG)
    prompt = f"Using this info: {knowledge}, answer the question: {query}"
    
    # 3. GENERATE (The 'G' in RAG)
    return f"AI says: {knowledge}" # Simplified

print(rag_simulation("What is Project Blue?"))
```

## When to use it
- When you want AI to answer questions about your private PDFs or emails.
- When you need the AI to stay up-to-date with real-time news.
- When you want to reduce "hallucinations" (incorrect facts).

## Related skills
- [Embeddings](../embeddings)
- [Vector Databases](../vector-databases)

[**← Back to Learning Path**](../../LEARNING_PATH.md)
