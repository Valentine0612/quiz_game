from fastapi import FastAPI
from app.routers import question

app = FastAPI()

app.include_router(question.router)
