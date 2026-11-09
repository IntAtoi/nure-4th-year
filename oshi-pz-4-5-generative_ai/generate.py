from ollama import generate

prompt_text = "Generate 200 words text about today news"

response_gemma = generate('gemma4:e2b', prompt=prompt_text)
content_gemma = response_gemma['response']
print("Gemma4")
print(content_gemma)

with open('generate_gemma4.txt', 'w', encoding='utf-8') as file:
    file.write(content_gemma)

response_qwen = generate('qwen3-vl:2b', prompt=prompt_text)
content_qwen = response_qwen['response']
print("\nQwen3-vl")
print(content_qwen)

with open('generate_qwen3.txt', 'w', encoding='utf-8') as file:
    file.write(content_qwen)