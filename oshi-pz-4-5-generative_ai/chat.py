from ollama import chat

messages = [
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
]

response_gemma = chat('gemma4:e2b', messages=messages)
content_gemma = response_gemma['message']['content']
print("Gemma4")
print(content_gemma)

with open('chat_gemma4.txt', 'w', encoding='utf-8') as file:
    file.write(content_gemma)

response_qwen = chat('qwen3-vl:2b', messages=messages)
content_qwen = response_qwen['message']['content']
print("\nQwen3-vl")
print(content_qwen)

with open('chat_qwen3.txt', 'w', encoding='utf-8') as file:
    file.write(content_qwen)