from fastapi import APIRouter

from controllers import ShareController

router = APIRouter()

router.include_router(ShareController.router, prefix='/shares')