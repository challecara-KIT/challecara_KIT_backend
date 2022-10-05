from typing import List
from fastapi import APIRouter, Depends, HTTPException
from schemas.friends import Friend, FriendPayload, TagColor, UpdatePayload
import cruds.friends as cf
from db.database import get_db
from utils.utils import get_current_user
from sqlalchemy.orm.session import Session

friend_router = APIRouter()

@friend_router.get("/", response_model=List[Friend])
async def get_all_friend(db: Session = Depends(get_db),user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    friends = cf.get_all_friends_by_id(db, user_id)
    return friends

@friend_router.post("/",response_model=Friend)
async def create_friend(
    friend_payload: FriendPayload, 
    tag_color: TagColor,
    db: Session = Depends(get_db), 
    user_id: str = Depends(get_current_user)
):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    friend = cf.create_friends_from_details(db,friend_payload.name, friend_payload.date, tag_color,user_id)
    return friend

@friend_router.put("/",response_model=Friend)
async def update_friend(
    up: UpdatePayload,
    tag_color: TagColor,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    friend = cf.update_friend_from_details(
        db, tag_color, up.name, up.friend_id, up.date, up.date_id
    )
    return friend


@friend_router.delete("/{friend_id}")
async def delete_friend(friend_id: str, db: Session = Depends(get_db),user_id: str = Depends(get_current_user)):
    if user_id is None:
        raise HTTPException(status_code=403, detail="jwt_token is invalid")
    cf.delete_friend_by_id(db, friend_id)
    return {"detail" : "OK!!"}
