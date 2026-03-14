from scheme_advisor_rag.services.vector_store import get_vector_store


# -------------------------
# Load FAISS Index
# -------------------------

def load_vector_store():
    return get_vector_store()


# -------------------------
# Ask Question
# -------------------------

def ask_question(query):

    vector_store = load_vector_store()

    results = vector_store.similarity_search(
        query,
        k=5
    )

    print("\n🔎 Top Scheme Recommendations:\n")

    for i, doc in enumerate(results):

        print(f"Result {i+1}")
        print("-----------------------------------")
        print(doc.page_content)
        print("\nMetadata:", doc.metadata)
        print("\n")


# -------------------------
# Chat Loop
# -------------------------

def start_chat():

    print("🤖 Government Scheme Advisor AI")
    print("Type 'exit' to stop\n")

    while True:

        query = input("Ask your question: ")

        if query.lower() == "exit":
            break

        ask_question(query)


# -------------------------
# Run Program
# -------------------------

if __name__ == "__main__":
    start_chat()