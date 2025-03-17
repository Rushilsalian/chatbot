from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
from thefuzz import process 

app = Flask(__name__)
CORS(app)

# Load dataset
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "data", "bbc-text.xlsx")

df = pd.read_excel(file_path)
df.rename(columns=lambda x: x.strip().lower(), inplace=True)  

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        user_query = data.get("query", "").strip().lower()

        if not user_query:
            return jsonify({"error": "Query cannot be empty"}), 400

        # Get best matching category
        categories = df["category"].unique().tolist()
        best_match, score = process.extractOne(user_query, categories)

        if score < 60:  # Adjust this threshold if needed
            return jsonify({"response": "No relevant category found."})

        # Get responses for the best matching category
        matched_texts = df[df["category"].str.lower() == best_match]["text"].tolist()

        return jsonify({"response": matched_texts})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
