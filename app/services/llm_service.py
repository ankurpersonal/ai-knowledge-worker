import ollama
from app.utils.logger import log_prompt

SYSTEM_PROMPT = "You are a helpful AI assistant."

def ask_llm(question: str):

    response = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ],
        options={
            "temperature": 0.9,
            "num_predict": 100
        }
    )

    answer = response["message"]["content"]

    log_prompt(question, answer)

    return answer