from fastapi import FastAPI
from app.routes import health

app = FastAPI(title="PaperTrail AI")

app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Welcome to PaperTrail AI by Mini"}