from fastapi import APIRouter, Depends, HTTPException
from schemas.clothes import SizeType,Clothe,ClothePayload,Season

from sqlalchemy.orm.session import Session
from db.database import get_db
from utils.utils import get_current_user
import cruds.clothes as cl
from utils.image import tagging_image

clothe_router = APIRouter()

@clothe_router.post("/",response_model=Clothe)
async def create_clothe(size: SizeType,season: Season ,payload: ClothePayload, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    result = tagging_image(payload.image_url)
    clothe = cl.create_clothe_by_payload(db, user_id, result["url"], size, result["type"], season, payload.color)
    return clothe

@clothe_router.delete("/{clothe_id}")
async def delete_clothe(clothe_id:str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    cl.delete_clothe_by_id(db,clothe_id)
    return {"detail" : "OK!!"}

@clothe_router.get("/{clothe_id}",response_model=Clothe)
async def get_clothe(clothe_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    clothe = cl.find_clothe_by_id(db,clothe_id)
    return clothe
