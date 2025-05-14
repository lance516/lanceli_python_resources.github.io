import requests
from time import sleep

with open("openrouter-api-key.txt", "r") as file:
    api_key = file.read().strip()

url = "https://openrouter.ai/api/v1/chat/completions"

messages = [
    {
        "role": "user",
        "content": "What is hello world?"
    }
]

token_used=0.0

payload = { 
    "model": "google/gemini-2.0-flash-001" ,
    "messages": messages
}
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
for i in range(100):
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    print("Google Gemini 2.0 Flash Response:")
    print(data["choices"][0]["message"]["content"])
    this_token = float(data["usage"]["total_tokens"])
    token_used+=this_token
    print(f"This time token: {this_token}")
    sleep(1)
print(f"total token used: {token_used}")