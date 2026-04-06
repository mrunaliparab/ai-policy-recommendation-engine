from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def recommend_policy(user_data):
    # Mock logic (replace with FAISS + embeddings)
    if user_data['age'] > 40:
        return {"policy": "Senior Life Plan"}
    return {"policy": "Standard Health Plan"}
