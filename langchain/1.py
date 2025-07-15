from openai import OpenAI
import os
# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())

client = OpenAI(
    base_url="https://api.deepseek.com/v1",
    api_key = os.getenv('DEEPSEEK_API_KEY')
)
def get_completion(prompt, model="deepseek-chat"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

prompt = "What is the capital of France?"
response = get_completion(prompt)
print(response)
    