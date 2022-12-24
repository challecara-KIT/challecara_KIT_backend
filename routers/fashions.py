from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from utils.utils import get_current_user
from db.database import get_db
from cruds.fashions import create_fashion, delete_fashion_by_id, get_my_all_fashion,recommend_fashion_by_date
from schemas.fashions import Fashion, FashionPayload

fashion_router = APIRouter()

@fashion_router.get("/",response_model=list[Fashion])
async def get_my_fashion(db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    fashions = get_my_all_fashion(db, user_id)
    return fashions

@fashion_router.post("/", response_model=Fashion)
async def create_my_fashion(
    name: str, 
    payload: FashionPayload, 
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    fashion = create_fashion(db,user_id,payload.clothe_ids,name,payload.date)
    return fashion

@fashion_router.delete("/{fashion_id}")
async def delete_my_fashion(fashion_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    delete_fashion_by_id(db,fashion_id)
    return {"message": "OK"}

@fashion_router.get("/recommend", response_model=list[Fashion])
async def get_my_recommend_fashion(db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    recommend = recommend_fashion_by_date(db, user_id)
    return recommend