#!/usr/bin/env python3
"""Simple CLI for chat via the OpenRouter API.

The script reads ``OPENROUTER_API_KEY`` from the environment or an ``.env``
file and uses the free Meta Llama 3 8B Instruct model by default. A system
prompt ensures the assistant behaves as **Ruyaa**, a professional helper.
"""
import os
import sys

from dotenv import load_dotenv
import requests

load_dotenv()

API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "meta-llama/llama-3-8b-instruct:free"
DEFAULT_SYSTEM_PROMPT = (
    "You are Ruyaa, a professional assistant. Provide clear, concise and helpful"
    " replies."
)

# Allow overrides via environment variables
MODEL = os.getenv("OPENROUTER_MODEL", DEFAULT_MODEL)
SYSTEM_PROMPT = os.getenv("OPENROUTER_SYSTEM_PROMPT", DEFAULT_SYSTEM_PROMPT)


def chat(messages, model=MODEL, system_prompt=SYSTEM_PROMPT):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    if system_prompt:
        messages = [{"role": "system", "content": system_prompt}] + messages

    payload = {"model": model, "messages": messages}
    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"].strip()


def main():
    if len(sys.argv) < 2:
        print("Usage: python openrouter_chat.py 'Your message'")
        sys.exit(1)

    user_content = " ".join(sys.argv[1:])
    messages = [{"role": "user", "content": user_content}]
    try:
        reply = chat(messages)
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)
    print(reply)


if __name__ == "__main__":
    main()
