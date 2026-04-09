from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.schemas import QuestionRequest
from app.services.stream_service import stream_llm

router = APIRouter()


@router.post("/chat-stream")
def chat_stream(request: QuestionRequest):

    generator = stream_llm(
        request.session_id,
        request.question
    )

    return StreamingResponse(
        generator,
        media_type="text/plain"
    )