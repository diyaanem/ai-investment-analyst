import os

BASE_PATH = "data/vector_store"

INDEX_FILE = os.path.join(BASE_PATH, "faiss_index.index")
CHUNKS_FILE = os.path.join(BASE_PATH, "chunks.pkl")


def reset_index():

    print("RESETTING VECTOR STORE...")

    if os.path.exists(INDEX_FILE):
        os.remove(INDEX_FILE)
        print("Deleted:", INDEX_FILE)
    else:
        print("Index not found")

    if os.path.exists(CHUNKS_FILE):
        os.remove(CHUNKS_FILE)
        print("Deleted:", CHUNKS_FILE)
    else:
        print("Chunks file not found")
