def chunk_documents(documents, chunk_size=500):

    chunks = []

    for doc in documents:

        for i in range(0, len(doc), chunk_size):
            chunks.append(doc[i:i+chunk_size])

    return chunks
