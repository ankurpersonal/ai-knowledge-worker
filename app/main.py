from fastapi import FastAPI
from app.routes.ask import router as ask_router

app = FastAPI(
    title="AI Knowledge Worker"
)

app.include_router(ask_router)