from fastapi import APIRouter
from .users import user_router
from .clothes import clothe_router

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(clothe_router, prefix="/clothes", tags=["clothes"])