from openai import OpenAI
from utils.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

text = "Revenue declined due to high operating costs."

embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input=text
)

print(len(embedding.data[0].embedding))
print(embedding.data[0].embedding[:10])
