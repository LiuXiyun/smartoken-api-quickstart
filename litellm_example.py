"""Make one billable text request through LiteLLM's OpenAI-compatible adapter."""
import os
from litellm import completion

response = completion(
    model='openai/deepseek-v4.1-flash',
    api_base=os.environ.get('SMTOKEN_BASE_URL', 'https://thesmartoken.com/v1'),
    api_key=os.environ['SMTOKEN_API_KEY'],
    messages=[{'role': 'user', 'content': 'Say hello in one sentence.'}],
    max_tokens=100,
    extra_body={"thinking": {"type": "disabled"}},
    num_retries=0,
    timeout=60,
)
print(response.choices[0].message.content)
if response.usage:
    print(f'Tokens: {response.usage.total_tokens}')
