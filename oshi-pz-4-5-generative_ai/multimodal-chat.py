from ollama import chat

path = r'E:\mgnat\desktop\NURE-4th-year\oshi-pz-4-5-generative_ai\bear.jpg'

messages = [
    {
        'role': 'user',
        'content': 'Describe what is in this image.',
        'images': [path],
    }
]

response_gemma = chat(
    model='gemma4:e2b',
    messages=messages,
)
content_gemma = response_gemma.message.content

print("Gemma4")
print(content_gemma)

with open('multimodal_gemma4.txt', 'w', encoding='utf-8') as file:
    file.write(content_gemma)

response_qwen = chat(
    model='qwen3-vl:2b',
    messages=messages,
)
content_qwen = response_qwen.message.content

print("\nQwen3-vl")
print(content_qwen)

with open('multimodal_qwen3.txt', 'w', encoding='utf-8') as file:
    file.write(content_qwen)