"""
Title: The 'Predictive Text' Demo
Description: This script simulates how an AI (like an LLM) predicts the next word based on patterns.
Usage: python pattern_finder.py
"""

import time

def simulate_ai_prediction(context):
    print(f"Context: '{context}'...")
    time.sleep(1) # Simulating 'thinking'
    
    # In a real AI, this would be a complex math function.
    # Here, we show how context dictates the prediction.
    patterns = {
        "The sky is": "Blue",
        "Hello, how are": "You",
        "The best programming language is": "Python (maybe!)",
        "Coffee is best served": "Hot"
    }
    
    prediction = patterns.get(context, "I don't know that pattern yet!")
    return prediction

if __name__ == "__main__":
    test_contexts = [
        "The sky is",
        "Hello, how are",
        "Coffee is best served"
    ]
    
    print("--- 🤖 Starting AI Simulation ---")
    for ctx in test_contexts:
        result = simulate_ai_prediction(ctx)
        print(f"Prediction: {result}\n")
    print("--- 🏁 Simulation Complete ---")
