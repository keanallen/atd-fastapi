from fastapi import FastAPI
from app.core.config import settings

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": f"Welcome to the {settings.project_name}!"}