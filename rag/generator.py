from openai import OpenAI
from utils.config import OPENAI_API_KEY
from rag.retriever import retrieve

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_answer(query):
    retrieved = retrieve(query)

    context_blocks = []
    for idx, text in retrieved:
        context_blocks.append(f"[Chunk {idx}]\n{text}")

    context = "\n\n".join(context_blocks)

    prompt = f"""
You are a professional investment analyst.

Answer using ONLY the context below.

Requirements:
- Use bullet points.
- Cite sources like [Chunk X].
- If not found, say "Not found in report."

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content
