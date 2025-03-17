from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load FAISS index
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

def get_response(query):
    """Fetch relevant documents from FAISS based on the query"""
    docs = vector_store.similarity_search(query, k=3)  # Retrieve top 3 results
    response = "\n\n".join([f"🔹 {doc.page_content} (Category: {doc.metadata['category']})" for doc in docs])
    return response if response else "Sorry, I couldn't find relevant information."

# Example usage
if __name__ == "__main__":
    while True:
        user_input = input("Ask something (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        print("\n🤖 Chatbot Response:\n", get_response(user_input))
