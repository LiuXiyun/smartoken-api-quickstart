# SmarToken API quickstart

Examples for SmarToken's OpenAI-compatible **text Chat Completions** API. Use your own SmarToken API key; keep it secret, store it server-side, and never commit it.

- [Create an account and API key](https://thesmartoken.com/register?utm_source=github&utm_medium=repository&utm_campaign=api_quickstart)
- [Documentation](https://thesmartoken.com/docs) · [Pricing](https://thesmartoken.com/pricing) · [Current model IDs](https://thesmartoken.com/v1/models)

**These examples send real billable requests.** New accounts start without an API balance; add funds before calling. Check current availability and pricing first. [Terms](https://thesmartoken.com/terms) · [Privacy](https://thesmartoken.com/privacy).

```sh
export SMTOKEN_API_KEY='your-key'
```

Use a key with a small daily and monthly budget when testing. Do not paste keys into a public issue, terminal recording, or source file. Each SDK example below sends one short non-streaming request with thinking disabled for the selected DeepSeek model.

## Python without an SDK

```sh
python3 quickstart.py
```

## OpenAI Python SDK

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install 'openai>=3,<4'
python openai_example.py
```

## OpenAI JavaScript SDK

Requires Node.js 18 or newer.

```sh
npm ci
node openai_example.mjs
```

## LiteLLM

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install 'litellm>=1.109,<1.110'
python litellm_example.py
```

The LiteLLM example uses its `openai/` compatible adapter with the SmarToken base URL; it does not claim a named native LiteLLM provider integration. Do not assume LiteLLM cost estimates reflect your bill; consult the SmarToken pricing and usage pages.

## Capabilities and errors

These are text Chat Completions examples. SmarToken also documents streaming; tool calling, structured output, and multimodal inputs are not supported by this API. Other OpenAI endpoints and arbitrary request parameters are not implied. Select model IDs from the live model list rather than assuming availability.

A 401 typically means the key is invalid or revoked; check that `SMTOKEN_API_KEY` is set in the same shell. Insufficient balance or key budgets can prevent a call. For a timeout or server error, the outcome may be unknown: **check the SmarToken request and usage logs before considering another call**. SDK examples disable automatic retries; network errors do not establish whether upstream processing or billing occurred.

The default base URL is `https://thesmartoken.com/v1`. `SMTOKEN_BASE_URL` is an optional override for controlled tests; only set it to a server you trust because it receives your API key and prompt. Production examples should use the default.
