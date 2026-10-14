from urllib import response

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
     base_url=os.getenv("BASE_URL"),
     api_key=os.getenv("API_KEY")
)

while True:
     user_input = input("User: ")

     if user_input.lower()  in ["exit", "quit"]:
         break

     response = client.chat.completions.create(
         model=os.getenv("MODEL"),
         messages=[
              {
                   "role":"user",
                   "content":user_input
              }
         ]

        )
     print("LLM Response: "+response.choices[0].message.content)

