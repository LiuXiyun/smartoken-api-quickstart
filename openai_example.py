import os
from openai import OpenAI

client = OpenAI(api_key=os.environ['SMTOKEN_API_KEY'], base_url='https://thesmartoken.com/v1')
response = client.chat.completions.create(
    model='deepseek-v4.1-flash',
    messages=[{'role': 'user', 'content': 'Say hello in one sentence.'}],
    max_tokens=100,
)
print(response.choices[0].message.content)
