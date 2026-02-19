from openai import OpenAI
from utils.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a financial analyst."},
        {"role": "user", "content": "Explain EBITDA in simple terms."}
    ]
)

print(response.choices[0].message.content)
