import os
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    #base_url="https://ollama.com/v1",
    api_key='d5f7383bd069439485a2974ed929741d.mUDPlWXl5pv2vxB8olOOZAxW'
)

response = client.chat.completions.create(
    model="gemma4:31b",
    messages=[{"role": "user", "content": "Say hello in one sentence."}],
)
# print(response)
print(response.choices[0].message.content)