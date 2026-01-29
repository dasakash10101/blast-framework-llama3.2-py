import requests
import json
import sys

def verify_ollama_codepilot():
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.2",
        "prompt": "Are you ready to generate test cases? Reply with YES.",
        "stream": False
    }
    
    print(f"Testing connection to {url} with model 'llama3.2'...")
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        data = response.json()
        actual_response = data.get("response", "").strip()
        print(f"Response Received: {actual_response}")
        
        if response.status_code == 200:
            print("✅ Handshake Successful: Ollama is ready.")
        else:
            print(f"❌ Handshake Failed: Status Code {response.status_code}")
            sys.exit(1)
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Is Ollama running?")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        # Check if model missing is the issue
        if "model" in str(e) or (response and "model" in response.text): 
             print("Hint: You might need to run 'ollama pull llama3.2'")
        sys.exit(1)

if __name__ == "__main__":
    verify_ollama_codepilot()
