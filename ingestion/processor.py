from ingestion.pdf_reader import extract_text_from_pdf
from ingestion.chunker import chunk_text
from rag.vector_store import build_faiss_index


def ingest_document(file_path: str):
    """
    Extract text, chunk it, and build FAISS index.
    """

    print("Extracting text...")

    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    print("Chunking text...")
    chunks = chunk_text(text)

    print(f"Total chunks: {len(chunks)}")

    print("Building FAISS index...")
    build_faiss_index(chunks)

    print("Ingestion complete.")
