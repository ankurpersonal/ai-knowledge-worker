# In-memory chat storage

chat_sessions = {}

SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a helpful AI assistant."
}

MAX_HISTORY = 10


def get_session(session_id):

    if session_id not in chat_sessions:

        chat_sessions[session_id] = [SYSTEM_PROMPT]

    return chat_sessions[session_id]


def add_message(session_id, role, content):

    if session_id not in chat_sessions:

        chat_sessions[session_id] = [SYSTEM_PROMPT]

    chat_sessions[session_id].append(
        {
            "role": role,
            "content": content
        }
    )

    # Keep last messages only
    if len(chat_sessions[session_id]) > MAX_HISTORY:

        chat_sessions[session_id] = (
            [SYSTEM_PROMPT]
            + chat_sessions[session_id][-MAX_HISTORY:]
        )