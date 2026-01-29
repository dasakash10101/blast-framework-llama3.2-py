import requests
import json
import os

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "testcase_template.md")

def load_template():
    try:
        with open(TEMPLATE_PATH, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Template not found."

def generate_test_cases(user_input):
    template = load_template()
    if template == "Template not found.":
        return {"error": "Template file missing."}
    
    # Construct the Prompt
    system_prompt = "You are an expert QA Engineer specialized in BDD. Your task is to generate high-quality Gherkin scenarios (Given/When/Then) based on the user's input. You MUST include Test Case IDs (e.g., @TC01) and Priority levels (e.g., @P1, @P2) as tags above each scenario. Follow the provided format exactly. Do not include preamble or conversational filler. Output ONLY the Gherkin scenarios."
    
    full_prompt = f"""
{system_prompt}

TEMPLATE STRUCTURE:
{template}

USER INPUT:
{user_input}

INSTRUCTIONS:
1. Analyze the USER INPUT to understand the feature.
2. Fill out the TEMPLATE STRUCTURE with realistic test cases (Positive, Negative, Edge).
3. Output the result in Markdown.
"""

    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.2",
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": 0.7
        }
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return {"response": data.get("response", "")}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Test run
    print(generate_test_cases("Login page with email and password"))
