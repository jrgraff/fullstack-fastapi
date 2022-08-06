from fastapi import APIRouter

from controllers import share_controller

router = APIRouter()

router.include_router(share_controller.router, prefix='/shares')