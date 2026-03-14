from fastapi import FastAPI
from pydantic import BaseModel
import os

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from transformers import pipeline

app = FastAPI(title="AI Government Scheme Advisor")

# -------------------------
# Global variables
# -------------------------

embeddings = None
vector_store = None
llm = None


# -------------------------
# Load models AFTER server starts
# -------------------------

@app.on_event("startup")
def load_models():
    global embeddings, vector_store, llm

    print("Loading embeddings...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Loading FAISS index...")
    vector_store = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    print("Loading LLM...")
    llm = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_length=512
    )

    print("All models loaded successfully")


# -------------------------
# Request model
# -------------------------

class UserProfile(BaseModel):
    age: int
    income: float
    state: str
    occupation: str
    question: str


# -------------------------
# Routes
# -------------------------

@app.get("/")
def home():
    return {"message": "AI Scheme Advisor API running"}


@app.post("/recommend")
def recommend_schemes(user: UserProfile):

    query = f"""
    Age: {user.age}
    Income: {user.income}
    State: {user.state}
    Occupation: {user.occupation}
    Question: {user.question}
    """

    docs = vector_store.similarity_search(query, k=5)

    context = ""
    for doc in docs:
        context += doc.page_content + "\n"

    prompt = f"""
You are an expert Government Scheme Advisor.

User Profile:
{query}

Relevant Schemes:
{context}

Recommend the best schemes and explain briefly.
"""

    response = llm(prompt)

    return {
        "recommendation": response[0]["generated_text"]
    }


# -------------------------
# IMPORTANT FOR RENDER
# -------------------------

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 10000))

    uvicorn.run(app, host="0.0.0.0", port=port)