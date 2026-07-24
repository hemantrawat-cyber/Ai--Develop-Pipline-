from ingestion.loader import load_documents
from ingestion.chunker import chunk_documents
from ingestion.embeddings import create_vector_store
from rag.pipeline import ask_ai
from security.guardrails import validate_prompt

def pipeline():

    print("Loading documents...")
    docs = load_documents("data/documents")

    print("Chunking...")
    chunks = chunk_documents(docs)

    print("Creating embeddings...")
    vector_db = create_vector_store(chunks)

    while True:
        question = input("Ask: ")

        if question.lower() == "exit":
            break

        if not validate_prompt(question):
            print("Blocked by security policy")
            continue

        answer = ask_ai(question, vector_db)

        print(answer)

if __name__ == "__main__":
    pipeline()
