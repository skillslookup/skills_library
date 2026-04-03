"""
Title: The 'ReAct' Agent Demo
Description: This script simulates an AI Agent's reasoning process (Thought -> Action -> Observation).
Usage: python react_agent.py
"""

import time

# 🔧 Mock Tools
def web_search(query):
    """Simulates a web search tool."""
    print(f"🌍 [TOOL: Web Search] Finding: {query}...")
    time.sleep(1)
    results = {
        "Paris weather": "Cloudy, 18°C (64°F)",
        "Deepmind mission": "To solve intelligence, to advance science and benefit humanity."
    }
    return results.get(query, "No results found.")

def calculator(expression):
    """Simulates a calculation tool."""
    print(f"🧮 [TOOL: Calculator] Solving: {expression}...")
    time.sleep(1)
    return eval(expression)

def agent_process(user_task):
    """Simulates the ReAct cycle."""
    print(f"\n🚀 New Task: {user_task}")
    
    # --- PHASE 1: REASONING ---
    print("🧠 [THOUGHT]: I need to check the current temperature in Paris and then convert it to Fahrenheit.")
    
    # --- PHASE 2: ACTION 1 (Search) ---
    search_result = web_search("Paris weather")
    print(f"📊 [OBSERVATION]: {search_result}")
    
    # --- PHASE 3: REASONING 2 ---
    print("🧠 [THOUGHT]: The temperature is 18°C. I should use the conversion formula (C * 9/5) + 32.")
    
    # --- PHASE 4: ACTION 2 (Calculate) ---
    calc_result = calculator("(18 * 9/5) + 32")
    print(f"📊 [OBSERVATION]: {calc_result}°F")
    
    # --- PHASE 5: FINAL ANSWER ---
    print(f"\n✅ [FINAL ANSWER]: The weather in Paris is 18°C, which is {calc_result}°F.")

if __name__ == "__main__":
    agent_process("Convert Paris weather to Fahrenheit")
