import os
import glob
import requests

global token_used
token_used = 0.0

# Read the API key from a file
with open("openrouter-api-key.txt", "r") as file:
    api_key = file.read().strip()

# Function to generate a summary for an article
def generate_summary(article_content):
    url = "https://openrouter.ai/api/v1/chat/completions"

    messages = [
        {
            "role": "user",
            "content": article_content
        },
        {
            "role": "system",
            "content": "Please summarize the above article in 100000 to 1000000 traditional chinese characters. Please do not include any other information or unrelated info, just directly output the summary. In your news please include some emojis"
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
    global token_used
    token_used += this_token
    
    return data["choices"][0]["message"]["content"]

# Path to the "articles" folder
articles_folder = "articles"
summaries_folder = "summaries"

# Create summaries folder if it doesn't exist
os.makedirs(summaries_folder, exist_ok=True)

# Use glob to get all files in the folder
article_files = glob.glob(os.path.join(articles_folder, "*"))

# Check if there are any files
if not article_files:
    print(f"No files found in the folder '{articles_folder}'.")
else:
    # Iterate through all files
    for file_path in article_files:
        # Ensure it's a file
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                article_content = file.read()
            
            # Generate summary for the article
            summary = generate_summary(article_content)
            
            # Print the summary
            print(f"Summary for '{os.path.basename(file_path)}':")
            print(summary)
            print("-" * 50)
            
            # Save the summary to the summaries folder
            newsname = os.path.splitext(os.path.basename(file_path))[0]
            summary_path = os.path.join(summaries_folder, f"{newsname}.txt")
            with open(summary_path, "w", encoding="utf-8") as summary_file:
                summary_file.write(summary)

# Print the total tokens used
print(f"Total tokens used: {token_used}")