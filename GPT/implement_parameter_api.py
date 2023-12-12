from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": "Tell me a fun fact."},
                {"role": "assistant", "content": "Sure, here is an interesting fact:"}
                ],
        temperature=0.6,
        max_tokens=30,
        top_p=0.8,
        frequency_penalty=0.6,
        presence_penalty=0.8
    )


print(response.choices[0].message.content)