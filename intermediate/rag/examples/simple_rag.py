"""
Title: The 'Open-Book' RAG Demo
Description: This script simulates how a RAG system retrieves private data to answer a query.
Usage: python simple_rag.py
"""

# 🗃️ Our 'Private' Knowledge Base
DATABASE = {
    "project_alpha": "Project Alpha is a 2025 initiative to build self-driving bicycles.",
    "company_policy": "All employees get free snacks on Fridays.",
    "holiday_schedule": "The office is closed on December 25th."
}

def retrieve_context(query):
    """Simple keyword-based retrieval (The 'R' in RAG)"""
    query = query.lower()
    for key, content in DATABASE.items():
        if any(word in query for word in key.split("_")):
            return content
    return "No matching document found in our private database."

def generate_answer(query, context):
    """Simulates sending both context AND query to an LLM (The 'A' and 'G' in RAG)"""
    print(f"\n--- 🧠 AI Brain Processing ---")
    print(f"Context Found: '{context}'")
    print(f"Question Asked: '{query}'")
    
    # In a real system, the LLM would summarize this.
    # Here, we show how the AI uses the context to answer correctly.
    if context != "No matching document found in our private database.":
        return f"Based on our internal documents: {context}"
    else:
        return "I don't have private info on that, so I can only use my general knowledge."

if __name__ == "__main__":
    test_queries = [
        "Tell me about Project Alpha",
        "When do we get free snacks?",
        "How do I fly a plane?" # Not in our DB
    ]
    
    for q in test_queries:
        context = retrieve_context(q)
        answer = generate_answer(q, context)
        print(f"✅ Final AI Answer: {answer}\n")
