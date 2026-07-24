from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4.1")

def ask_ai(question, vector_db):

    docs = vector_db.similarity_search(question, k=3)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

    return llm.invoke(prompt).content
