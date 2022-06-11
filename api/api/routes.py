from fastapi import FastAPI, Header, Response, Cookie
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    description: str
    value: float

items = []

@app.get("/")
async def read_root():
    return {"message": "Hello world!"}

@app.get("/header")
async def header(user_agent: Optional[str] = Header(None)):
    return {"user_agent": user_agent}

@app.get("/cookie")
async def post_cookie(response: Response):
    response.set_cookie(key="mycookie", value="123")
    return {"cookie": True}

@app.get("/get-cookie")
async def get_cookie(mycookie: Optional[str] = Cookie(None)):
    return {"Cookie": mycookie}

@app.get("/items/{item_id}")
async def query_item(item_id:int, desc: str, val: float):
    return {"id": item_id, "description": desc, "value": val}

@app.post("/items")
async def body_item(new_item: Item):
    return new_item