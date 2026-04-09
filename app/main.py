from fastapi import FastAPI

from app.routes.ask import router as ask_router
from app.routes.chat_stream import router as stream_router

app = FastAPI(
    title="AI Knowledge Worker"
)

app.include_router(ask_router)
app.include_router(stream_router)