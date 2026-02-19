from openai import OpenAI
from utils.vector_store import search_similar_chunks
from utils.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def answer_question(question: str, k: int = 5):
    # 1. Retrieve relevant chunks
    chunks = search_similar_chunks(question, k=k)

    context = "\n\n".join(chunks)

    # 2. Create prompt
    prompt = f"""
You are a financial analyst.

Use ONLY the provided context to answer the question.
If the answer is not in the context, say "Not found in report."

Context:
{context}

Question:
{question}

Answer:
"""

    # 3. Call GPT
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content
