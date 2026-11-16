# SmarToken API quickstart

Examples for SmarToken's OpenAI-compatible text Chat Completions API. Use your own SmarToken API key; keep it in a server-side environment variable and never commit it.

- [Get an API key](https://thesmartoken.com/dashboard/api-keys)
- [Documentation](https://thesmartoken.com/docs) · [Pricing](https://thesmartoken.com/pricing) · [Current model IDs](https://thesmartoken.com/v1/models)

New accounts require a positive balance before calling the API. Check the model list and current pricing before use. Availability and prices may change.

```sh
export SMTOKEN_API_KEY='your-key'
python3 quickstart.py
```

The Python example uses the standard library. To use the official OpenAI Python SDK instead, install `openai` and run `python3 openai_example.py`.

The gateway supports text Chat Completions with JSON or SSE streaming. Tool calling, structured-output APIs and multimodal inputs are not supported. Do not assume compatibility with every OpenAI endpoint or agent tool. Keys are specific to SmarToken and do not work with other providers.

The examples make real billable requests. See [pricing](https://thesmartoken.com/pricing), [terms](https://thesmartoken.com/terms), and [privacy](https://thesmartoken.com/privacy).
