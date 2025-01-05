import requests

# Set your Groq API key and endpoint
API_KEY = "your_groq_api_key_here"
API_ENDPOINT = "https://api.groq.com/v1/completions"  # Replace with Groq's actual endpoint

# Function to interact with the LLM via Groq API
def interact_with_llm(prompt):
    try:
        # Prepare the payload
        payload = {
            "prompt": prompt,
            "max_tokens": 100,  # Limit the response length
            "temperature": 0.7  # Adjust for creativity
        }
        
        # Set headers with the API key
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        # Send the request
        response = requests.post(API_ENDPOINT, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Extract and return the response text
        return response.json().get("choices", [{}])[0].get("text", "No response")
    
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    prompt = input("Enter your question or prompt: ")
    response = interact_with_llm(prompt)
    print("\nResponse:\n", response)
