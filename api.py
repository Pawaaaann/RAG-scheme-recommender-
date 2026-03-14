from fastapi import FastAPI
from pydantic import BaseModel

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from transformers import pipeline

# -------------------------
# Initialize FastAPI
# -------------------------

app = FastAPI(title="AI Government Scheme Advisor")


# -------------------------
# Load Embeddings
# -------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -------------------------
# Load Vector Database
# -------------------------

vector_store = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# -------------------------
# Load LLM
# -------------------------

llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=512
)


# -------------------------
# Request Model
# -------------------------

class UserProfile(BaseModel):

    age: int
    income: float
    state: str
    occupation: str
    question: str


# -------------------------
# API Endpoint
# -------------------------

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