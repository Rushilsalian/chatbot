from flask import Flask, request, jsonify
from flask_cors import CORS
from vector_store import get_response_from_pdf
from src.chatbot import text_to_speech, speech_to_text

app = Flask(__name__)
CORS(app)

chat_history = []

@app.route("/ask", methods=["POST"])
def ask():
    """Handle text-based queries."""
    try:
        data = request.get_json()
        user_query = data.get("query", "").strip()

        if not user_query:
            return jsonify({"error": "Query cannot be empty"}), 400

        response = get_response_from_pdf(user_query)

        chat_history.append({"query": user_query, "response": response})

        return jsonify({
            "response": response,
            "history": chat_history
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/ask-voice", methods=["GET"])
def ask_voice():
    """Handle voice queries."""
    try:
        user_query = speech_to_text()
        response = get_response_from_pdf(user_query)
        text_to_speech(response)

        chat_history.append({"query": user_query, "response": response})

        return jsonify({
            "query": user_query,
            "response": response,
            "history": chat_history
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get-chats", methods=["GET"])
def get_chats():
    """Get the current chat history."""
    try:
        return jsonify({
            "history": chat_history
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/delete-chat", methods=["POST"])
def delete_chat():
    try:
        data = request.get_json()
        index = data.get("index")

        if index is None or not (0 <= index < len(chat_history)):
            return jsonify({"error": "Invalid index"}), 400

        chat_history.pop(index)

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
