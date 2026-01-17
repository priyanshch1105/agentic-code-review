from fastapi import FastAPI
from app.api.webhook import router

app = FastAPI(title="Agentic Code Review")

app.include_router(router)

@app.get("/")
def health():
    return {"status": "ok"}
