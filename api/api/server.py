import uvicorn
from fastapi import FastAPI

from api.routes import router

app = FastAPI()
app.include_router(router, prefix='')

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("api.server:app", host="0.0.0.0", port=8000, reload=True)