import ormar
from fastapi import APIRouter, Response

from models.share import Share

router = APIRouter()

@router.get("/")
async def show_shares():
  return await Share.objects.all()

@router.post("/")
async def create_share(share: Share):
  await Share.save(share)
  return share

@router.get("/{share_id}")
async def get_share_by_id(share_id: int, response: Response):
  try:
    return await Share.objects.get(id=share_id)
  except ormar.exceptions.NoMatch:
    response.status_code = 404
    return {"message": "Share not found"}