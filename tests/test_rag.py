from ingestion.processor import ingest_document
from rag.generator import generate_answer

# 1️⃣ Ingest the report (loads into vector store)
ingest_document("data/raw/acme_annual_report.txt")

# 2️⃣ Ask a question
question = "What were ACME Corp's main revenue drivers in 2023?"

answer = generate_answer(question)

print("\n=== QUESTION ===\n")
print(question)

print("\n=== ANSWER ===\n")
print(answer)
