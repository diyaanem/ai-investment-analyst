import numpy as np
import os
import faiss
import pickle
from openai import OpenAI
from utils.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def create_embeddings(text_chunks):
    embeddings = []
    for chunk in text_chunks:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        )
        embeddings.append(response.data[0].embedding)

    return embeddings


def build_faiss_index(chunks, save_path="data/vector_store"):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    print("Creating embeddings...")
    embeddings = create_embeddings(chunks)

    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings).astype("float32"))

    # Save index
    faiss.write_index(index, os.path.join(save_path, "faiss_index.index"))

    # Save chunks separately
    with open(os.path.join(save_path, "chunks.pkl"), "wb") as f:
        pickle.dump(chunks, f)

    print("FAISS index built and saved.")
