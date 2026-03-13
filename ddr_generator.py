import requests

API_KEY = "your api key here"

def generate_ddr(report1_text, report2_text):

    with open("prompts.txt", "r") as f:
        system_prompt = f.read()

    prompt = f"""
{system_prompt}

Report 1:
{report1_text}

Report 2:
{report2_text}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-3.1-8b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    data = response.json()
    return data["choices"][0]["message"]["content"]