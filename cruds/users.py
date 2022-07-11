import bcrypt
import os
from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from schemas.users import User as UserSchema
from db.model import User

salt = os.environ.get('PASSWORD_HASH_SALT',
                      '$2a$10$ThXfVCPWwXYx69U8vuxSUu').encode()


def gen_password_hash(password: str):
    hash = bcrypt.hashpw(password.encode(), salt)
    return hash.decode()


def create_user(db: Session, name: str, email: str, password: str) -> UserSchema:
    same_name_user = db.query(User).filter(User.email == email).first()
    if same_name_user is not None:
        raise HTTPException(
            status_code=400, detail="this email is already used")

    password_hash = gen_password_hash(password)

    user_orm = User(
        name=name,
        email=email,
        password_hash=password_hash,
    )

    db.add(user_orm)
    db.commit()
    db.refresh(user_orm)

    user = UserSchema.from_orm(user_orm)
    return user


def get_user_by_id(db: Session, user_id: str) -> UserSchema:
    user_orm = db.query(User).get(user_id)
    if user_orm is None:
        raise HTTPException(status_code=400, detail='user not exist')
    user = UserSchema.from_orm(user_orm)

    return user


def get_user_by_name(db: Session, email: str) -> User:
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(
            status_code=400, detail='user has this email is not exist')
    return user


def delete_user_by_id(db: Session, user_id: str) -> None:
    user_orm = db.query(User).get(user_id)
    if user_orm is None:
        raise HTTPException(status_code=400, detail='user not exist')
    db.delete(user_orm)
    db.commit()
    return
