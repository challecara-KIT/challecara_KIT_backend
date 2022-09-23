from pydantic import BaseModel
from enum import Enum

class SizeType(str, Enum):
    ss = "SS"
    s = "S"
    m = "M"
    l = "L"
    ll = "LL"

class Clothe(BaseModel):
    clothe_id: str
    image_url: str
    size: str
    color: str
    user_id: str

    class Config:
        orm_mode = True
    
class ClothePayload(BaseModel):
    image_url: str
    color: str
    