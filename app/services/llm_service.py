import ollama

from app.utils.memory import (
    get_session,
    add_message
)

from app.utils.logger import log_prompt


def ask_llm(session_id: str, question: str):

    # Add user message first
    add_message(session_id, "user", question)

    # Get updated messages
    messages = get_session(session_id)

    response = ollama.chat(
        model="phi3:latest",
        messages=messages,
        options={
            "temperature": 0.7,
            "num_predict": 200
        }
    )

    answer = response["message"]["content"]

    # Add assistant reply
    add_message(session_id, "assistant", answer)

    log_prompt(question, answer)

    return answer