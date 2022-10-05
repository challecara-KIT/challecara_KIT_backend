from fastapi import APIRouter
from .users import user_router
from .clothes import clothe_router
from .friends import friend_router
from .fashions import fashion_router

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(clothe_router, prefix="/clothes", tags=["clothes"])
router.include_router(friend_router, prefix="/friends", tags=["friends"])
router.include_router(fashion_router, prefix="/fashions", tags=["fashions"])