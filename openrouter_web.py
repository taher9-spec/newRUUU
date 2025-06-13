from flask import Flask, request, jsonify, send_file
import os
from openrouter_chat import chat

app = Flask(__name__)



HTML_PATH = os.path.join(os.path.dirname(__file__), "public", "index.html")


@app.route("/")
def index():
    return send_file(HTML_PATH)


@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json()
    message = data.get("message", "") if data else ""
    if not message:
        return jsonify({"error": "message required"}), 400
    try:
        reply = chat([{"role": "user", "content": message}])
    except Exception as exc:
        app.logger.exception("Chat error")
        return jsonify({"error": str(exc)}), 500
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
