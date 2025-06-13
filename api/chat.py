"""Serverless chat endpoint for Vercel."""

from flask import Flask, request, jsonify

from openrouter_chat import chat

app = Flask(__name__)


@app.post("/")
def handle_chat() -> tuple[str, int] | tuple[dict, int]:
    """Handle a chat request.

    The function expects JSON with a ``message`` field and returns the reply
    from the OpenRouter API.
    """

    data = request.get_json() or {}
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "message required"}), 400

    try:
        reply = chat([{"role": "user", "content": message}])
    except Exception as exc:  # pragma: no cover - external call
        app.logger.exception("Chat error")
        return jsonify({"error": str(exc)}), 500

    return jsonify({"reply": reply}), 200


# ``app`` is picked up by Vercel's Python runtime
handler = app
