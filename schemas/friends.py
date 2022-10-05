from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from schemas.users import User

class TagColor(str,Enum):
    red = "red"
    orange = "orange"
    yellow = "yellow"
    green = "green"
    blue = "blue"
    indigo = "indigo"
    violet = "violet"

class FriendDate(BaseModel):
    date_id: str
    friend_id: str
    date: datetime

    class Config:
        orm_mode = True

class Friend(BaseModel):
    friend_id: str
    name: str
    tag_color: str
    user: User
    date: list[FriendDate]

    class Config:
        orm_mode = True

class FriendPayload(BaseModel):
    name: str
    date: datetime

class UpdatePayload(BaseModel):
    name: str
    friend_id: str
    date: Optional[datetime] = None
    date_id: Optional[str] = None