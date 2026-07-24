from pathlib import Path

def load_documents(path):

    docs = []

    for file in Path(path).glob("*.txt"):
        docs.append(file.read_text())

    return docs
