// One billable text request using the OpenAI JavaScript SDK.
import OpenAI from 'openai';

if (!process.env.SMTOKEN_API_KEY) throw new Error('Set SMTOKEN_API_KEY first');
const client = new OpenAI({
  apiKey: process.env.SMTOKEN_API_KEY,
  baseURL: process.env.SMTOKEN_BASE_URL || 'https://thesmartoken.com/v1',
  maxRetries: 0,
  timeout: 60_000,
});
const response = await client.chat.completions.create({
  model: 'deepseek-v4.1-flash',
  messages: [{ role: 'user', content: 'Say hello in one sentence.' }],
  max_tokens: 100,
  thinking: { type: "disabled" },
});
console.log(response.choices[0].message.content);
if (response.usage) console.log(`Tokens: ${response.usage.total_tokens}`);
