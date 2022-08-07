import uvicorn
from fastapi import FastAPI

from api.routes import router
from database.create_tables import config_db

app = FastAPI()
app.include_router(router, prefix='')

@app.get('/')
def get_root():
    return {'api': 'running'}

def config_database():
    config_db()

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("api.server:app", host="0.0.0.0", port=8000, reload=True)