import requests
from time import sleep

global token_used
token_used = 0.0

with open("openrouter-api-key.txt", "r") as file:
    api_key = file.read().strip()

def ask_ai(prompt, image_url=None):
    global token_used  # Ensure global variable is used

    url = "https://openrouter.ai/api/v1/chat/completions"

    if image_url:
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            }
        ]
    else: 
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

    payload = { 
        "model": "google/gemini-2.0-flash-001",
        "messages": messages
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    
    this_token = float(data["usage"]["total_tokens"])
    token_used += this_token
    
    return data["choices"][0]["message"]["content"]

if __name__ == "__main__":
    input_prompt = input("Enter your prompt: ")
    response = ask_ai(input_prompt)
    print("AI Response:")
    print(response)