from fastapi import APIRouter
from app.models.schemas import QuestionRequest
from app.services.llm_service import ask_llm

router = APIRouter()

@router.post("/ask")
def ask_question(request: QuestionRequest):

    answer = ask_llm(
        request.session_id,
        request.question
    )

    return {
        "session_id": request.session_id,
        "question": request.question,
        "answer": answer
    }