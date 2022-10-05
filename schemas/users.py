from pydantic import BaseModel, EmailStr
from schemas.clothes import Clothe
from schemas.fashions import Fashion

class SignUpPayload(BaseModel):
    name: str
    email: EmailStr
    password: str


class SignInPayload(BaseModel):
    email: EmailStr
    password: str


class User(BaseModel):
    user_id: str
    email: EmailStr
    name: str

    class Config:
        orm_mode = True


class AuthInfo(BaseModel):
    jwt: str


class UserClothes(BaseModel):
    user_id: str
    name: str
    clothes: list[Clothe]
    fashions: list[Fashion]

    class Config:
        orm_mode = True