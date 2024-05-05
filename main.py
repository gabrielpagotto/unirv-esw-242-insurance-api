from fastapi import FastAPI
from src.features.credit_score import handler as credit_score_handler

app = FastAPI(docs_url="/swagger")

app.include_router(credit_score_handler.router_v1)
