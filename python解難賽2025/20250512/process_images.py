import base64

import os
import glob
import requests

with open("openrouter-api-key.txt", "r") as file:
    api_key = file.read().strip()

files = glob.glob("images/*.jpg")
files += glob.glob("images/*.png")
files += glob.glob("images/*.jpeg") 

for file_path in files:
    # Read the image file
    with open(file_path, "rb") as image_file:
        # Encode the image to base64
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Create the payload for the API request
    payload = {
        "model": "google/gemini-2.0-flash-001",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is this? Provide a detailed description of the image."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_string}"
                        }
                    }
                ]
            }
        ]
    }

    
    # Make the API request
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload)
    
    # Print the response
    print(response.json())