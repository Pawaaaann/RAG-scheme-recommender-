from scheme_advisor_rag.services.llm import get_llm
from scheme_advisor_rag.services.vector_store import get_vector_store


# -------------------------
# Load Vector Store
# -------------------------

def load_vector_store():
    return get_vector_store()


# -------------------------
# Load LLM
# -------------------------

def load_llm():
    return get_llm()


# -------------------------
# Generate AI Answer
# -------------------------

def generate_answer(query):

    vector_store = load_vector_store()

    results = vector_store.similarity_search(query, k=5)

    context = ""

    for doc in results:
        context += doc.page_content + "\n"

    prompt = f"""
You are an expert Government Scheme Advisor.

User Question:
{query}

Available Schemes:
{context}

Based on the schemes above, recommend the best schemes and explain why.
"""

    llm = load_llm()

    response = llm(prompt)

    print("\n🤖 AI Recommendation:\n")
    print(response[0]["generated_text"])


# -------------------------
# Chat Loop
# -------------------------

def start_chat():

    print("🇮🇳 AI Government Scheme Advisor")
    print("Type 'exit' to quit\n")

    while True:

        query = input("Ask your question: ")

        if query.lower() == "exit":
            break

        generate_answer(query)


# -------------------------
# Run
# -------------------------

if __name__ == "__main__":
    start_chat()