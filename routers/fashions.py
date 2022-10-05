from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from utils.utils import get_current_user
from db.database import get_db
from cruds.fashions import create_fashion
from schemas.fashions import Fashion, FashionPayload

fashion_router = APIRouter()

@fashion_router.post("/", response_model=Fashion)
async def create_my_fashion(
    name: str, 
    payload: FashionPayload, 
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    fashion = create_fashion(db,user_id,payload.clothe_ids,name)
    return fashion