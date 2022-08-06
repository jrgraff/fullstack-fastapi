from fastapi import APIRouter

from models.share import Share

router = APIRouter()

@router.get("/")
async def show_shares():
  return await Share.objects.all()

@router.post("/")
async def create_share(share: Share):
  await Share.save(share)
  return share