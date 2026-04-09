import ollama

from app.utils.memory import (
    get_session,
    add_message
)

MODEL_NAME = "phi3:latest"


def stream_llm(session_id: str, question: str):

    # Add user message
    add_message(session_id, "user", question)

    messages = get_session(session_id)

    stream = ollama.chat(
        model=MODEL_NAME,
        messages=messages,
        stream=True
    )

    full_response = ""

    for chunk in stream:

        token = chunk["message"]["content"]

        full_response += token

        yield token

    # Save assistant response
    add_message(session_id, "assistant", full_response)