from datetime import datetime
from pydantic import BaseModel
from .clothes import Clothe

class FashionDate(BaseModel):
    date_id: str
    fashion_id: str
    date: datetime

    class Config:
        orm_mode = True

class Fashion(BaseModel):
    fashion_id: str
    user_id: str
    name: str
    clothes: list[Clothe]
    date: list[FashionDate]

    class Config:
        orm_mode = True
    
class FashionPayload(BaseModel):
    clothe_ids: list[str]
    

