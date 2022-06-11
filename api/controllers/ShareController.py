from fastapi import APIRouter

from models.Share import Share

router = APIRouter()

database = []

@router.get("/")
def show_shares():
  return database

@router.post("/")
def create_share(share: Share):
  database.append(share)
  return share