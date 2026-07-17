import os
from huggingface_hub import InferenceClient

os.environ["HF_TOKEN"] = "YOUR TOKEN KEY"

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"]
)

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "Reply with only: Hugging Face Connected"
        }
    ],
    max_tokens=20
)

print(response.choices[0].message.content)