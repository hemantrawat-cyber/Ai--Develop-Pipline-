from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def create_vector_store(chunks):

    embeddings = OpenAIEmbeddings()

    return FAISS.from_texts(chunks, embeddings)
