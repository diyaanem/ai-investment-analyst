from ingestion.processor import ingest_document
from rag.retriever import retrieve

# Build index
ingest_document("data/raw/acme_annual_report.txt")

# Test retrieval
results = retrieve("What were ACME Corp's main revenue drivers in 2023?")

print("\n=== RETRIEVED CHUNKS ===\n")

for i, chunk in enumerate(results):
    print(f"\n--- Chunk {i+1} ---\n")
    print(chunk)
