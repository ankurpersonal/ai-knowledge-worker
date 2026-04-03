from fastapi import APIRouter
from app.models.schemas import QuestionRequest
from app.services.llm_service import ask_llm

router = APIRouter()

@router.post("/ask")
def ask_question(request: QuestionRequest):

    answer = ask_llm(request.question)

    return {
        "question": request.question,
        "answer": answer
    }