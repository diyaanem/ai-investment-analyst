import faiss
import pickle
import time
import os
import numpy as np
from openai import OpenAI
from utils.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)



def load_vector_store(path="data/vector_store"):

    index_path = f"{path}/faiss_index.index"
    chunks_path = f"{path}/chunks.pkl"

    # 🔥 Force wait until files exist (important after rebuild)
    while not os.path.exists(index_path):
        time.sleep(0.5)

    # 🔥 Always reload fresh
    index = faiss.read_index(index_path)

    with open(chunks_path, "rb") as f:
        chunks = pickle.load(f)

    print("Loaded vector store from:", path)

    return index, chunks


def retrieve(query, top_k=3):
    index, chunks = load_vector_store()

    query_embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding

    query_vector = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    top_indices = indices[0]

    retrieved_chunks = [(int(i), chunks[int(i)]) for i in top_indices]

    return retrieved_chunks

