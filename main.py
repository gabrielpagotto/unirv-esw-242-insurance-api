from fastapi import FastAPI
from src.features.credit_score import handler as credit_score_handler

app = FastAPI()

app.include_router(credit_score_handler.router_v1)
