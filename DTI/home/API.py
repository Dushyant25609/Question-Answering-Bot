import requests
import re

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    json_data = response.json()
    
    generated_text = json_data[0]['generated_text'] if json_data else ''
    return generated_text


def prompt(Ques):
    prompt = f"Write the correct answer and only the necessary answer of the given question in in 50 to 100 words.{Ques}\n\n\n\nAnswer:\n\n\n"
    return prompt

# Example usage:
Ques = "what is the capital of India?"
prompt_text = prompt(Ques)
payload = {"inputs": prompt_text}
generated_text = query(payload)

# Removing the question from the generated text
question_index = generated_text.find(Ques)
if question_index != -1:
    answer = generated_text[question_index + len(Ques):].strip()
else:
    answer = generated_text


