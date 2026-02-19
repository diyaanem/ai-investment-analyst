import numpy as np
from utils.embeddings import get_embedding

# Simple in-memory store
VECTOR_DB = []


def add_chunk(text: str):
    embedding = get_embedding(text)
    VECTOR_DB.append({
        "text": text,
        "embedding": embedding
    })


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def search_similar_chunks(query: str, k: int = 5):
    query_embedding = get_embedding(query)

    scored = []
    for item in VECTOR_DB:
        score = cosine_similarity(query_embedding, item["embedding"])
        scored.append((score, item["text"]))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [text for _, text in scored[:k]]
