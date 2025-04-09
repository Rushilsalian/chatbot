from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load FAISS index
with open("models/faiss_index.pkl", "rb") as f:
    vector_store = pickle.load(f)

chat_history = []

@app.route('/ask', methods=['POST'])
def ask():
    """API endpoint to ask a question to the chatbot."""
    user_input = request.json.get("question", "")
    response = vector_store.similarity_search(user_input, k=1)[0].page_content
    return jsonify({"response": response})

@app.route('/get-chats', methods=['GET'])
def get_chats():
    """API endpoint to get past chats."""
    return jsonify({
        "history": chat_history
    })
    
if __name__ == '__main__':
    app.run(debug=True)
