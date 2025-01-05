import requests

API_KEY = "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"  

def interact_with_llm(prompt):
    try:
       
        payload = {
            "model": "llama-3.3-70b-versatile",  
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 100, 
            "temperature": 0.7  
        }
        
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)
        response.raise_for_status()  
        
      
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response")
    
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    prompt = input("Enter your question or prompt: ")
    response = interact_with_llm(prompt)
    print("\nResponse:\n", response)
