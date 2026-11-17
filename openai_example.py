"""Make one billable text request using the OpenAI Python SDK."""
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ['SMTOKEN_API_KEY'],
    base_url=os.environ.get('SMTOKEN_BASE_URL', 'https://thesmartoken.com/v1'),
    max_retries=0,
    timeout=60.0,
)
response = client.chat.completions.create(
    model='deepseek-v4.1-flash',
    messages=[{'role': 'user', 'content': 'Say hello in one sentence.'}],
    max_tokens=100,
    extra_body={"thinking": {"type": "disabled"}},
)
print(response.choices[0].message.content)
if response.usage:
    print(f'Tokens: {response.usage.total_tokens}')
