import json
import os
import urllib.request

key = os.environ['SMTOKEN_API_KEY']
request = urllib.request.Request(
    'https://thesmartoken.com/v1/chat/completions',
    data=json.dumps({'model': 'deepseek-v4.1-flash', 'messages': [{'role': 'user', 'content': 'Say hello in one sentence.'}], 'max_tokens': 100}).encode(),
    headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {key}'},
    method='POST',
)
with urllib.request.urlopen(request, timeout=60) as response:
    result = json.load(response)
print(result['choices'][0]['message']['content'])
