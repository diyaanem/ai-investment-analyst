import os
from rag.vector_store import build_faiss_index

# Load processed chunks
chunks = []
for file in sorted(os.listdir("data/processed")):
    with open(f"data/processed/{file}", "r", encoding="utf-8") as f:
        chunks.append(f.read())

build_faiss_index(chunks)
