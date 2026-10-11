from openai import OpenAI

client = OpenAI(
     base_url="http://127.0.0.1:11434/v1",
     api_key="dummy_api_key"
)

response = client.chat.completions.create(
    model="Qwen3:4b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
     #    {"role": "user", "content": "Hello! Can you help me with a question?"}
    ]

)

print("LLM Response: ")
print(response.choices[0].message.content)