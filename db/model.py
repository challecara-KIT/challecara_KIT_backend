from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4

Base = declarative_base()


def generate_uuid():
    return str(uuid4())


class User(Base):
    __tablename__ = 'users'
    user_id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String, nullable=True)
    clothes = relationship("Clothe")


class Clothe(Base):
    __tablename__ = "clothe"
    clothe_id = Column(String, primary_key=True, default=generate_uuid)
    image_url = Column(String, nullable=False)
    size = Column(String, nullable=False)
    color = Column(String, nullable=False)
    user_id = Column(String, ForeignKey("users.user_id"))
    