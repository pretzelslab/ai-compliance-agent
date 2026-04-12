import os
import anthropic

key = os.environ.get("ANTHROPIC_API_KEY", "")
print(f"Key length: {len(key)}")
print(f"Key prefix: {key[:8]}...")

client = anthropic.Anthropic(api_key=key)
msg = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=10,
    messages=[{"role": "user", "content": "hi"}]
)
print("API key: OK")
