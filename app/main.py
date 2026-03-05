from fastapi import FastAPI
from app.api.router import api_router
from app.core.config import settings

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": f"Welcome to the {settings.project_name}!"}