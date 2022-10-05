from typing import List, Optional
from fastapi import HTTPException
from datetime import datetime
from sqlalchemy.orm.session import Session
from db.model import Friend,FriendDate
import schemas.friends as sf

def create_friends_from_details(
    db: Session,
    name: str,
    date: datetime,
    tag_color: str,
    user_id: str
) -> sf.Friend : 
    same_friend = db.query(Friend).filter(Friend.name == name).first()
    if same_friend is None:
        friend_orm = Friend(
            name=name,
            tag_color=tag_color,
            user_id=user_id,
        )
        db.add(friend_orm)
        db.commit()
        db.refresh(friend_orm)
        date_orm = FriendDate(
            date=date,
            friend_id=friend_orm.friend_id
        )
        db.add(date_orm)
        db.commit()
        friend = sf.Friend.from_orm(friend_orm)
    else:
        date_orm = FriendDate(
            date=date,
            friend_id=same_friend.friend_id,
        )
        db.add(date_orm)
        db.commit()
        friend = sf.Friend.from_orm(same_friend)
    return friend


def update_friend_from_details(
    db: Session, 
    tag_color: str,
    name: str, 
    friend_id: str,
    date: Optional[datetime] = None,
    date_id: Optional[str] = None
) -> sf.Friend:
    friend_orm = db.query(Friend).filter(Friend.friend_id == friend_id).first()
    if friend is None:
        raise HTTPException(status_code=404, detail="friend not found!!")
    friend_orm.name = name
    friend_orm.tag_color = tag_color
    db.commit()
    if date is not None and date_id is not None:
        date_orm = db.query(FriendDate).filter(FriendDate.date_id == date_id).first()
        if date_orm is None:
            raise HTTPException(status_code=404, detail="date not found")
        date_orm.date = date
        db.commit()
    elif (date is None and date_id is not None) and (date is not None and date_id is None):
        raise HTTPException(status_code=400, detail="params Error")

    friend = sf.Friend.from_orm(friend_orm)
    return friend



def delete_friend_by_id(db: Session, friend_id: str) -> None:
    friend_orm = db.query(Friend).filter(Friend.friend_id == friend_id).first()
    if friend_orm is None:
        raise HTTPException(status_code=404, detail="friend not found!!")
    db.delete(friend_orm)
    db.commit()
    return


def get_all_friends_by_id(db: Session, user_id: str) -> List[sf.Friend]:
    friends_orm = db.query(Friend).filter(Friend.user_id == user_id).all()
    friends = list(map(sf.Friend.from_orm,friends_orm))
    return friends