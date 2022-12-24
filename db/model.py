from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, ForeignKey 
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
    fashions = relationship("Fashion")

class Fashion_Clothes(Base):
    __tablename__ = "fashion_clothes"
    fc_id = Column(String, primary_key=True, default=generate_uuid)
    clothe_id = Column(String, ForeignKey("clothes.clothe_id"))
    fashion_id = Column(String, ForeignKey("fashions.fashion_id"))


class Clothe(Base):
    __tablename__ = "clothes"
    clothe_id = Column(String, primary_key=True, default=generate_uuid)
    image_url = Column(String, nullable=False)
    size = Column(String, nullable=False)
    color = Column(String, nullable=False)
    type = Column(String)
    season = Column(String)
    user_id = Column(String, ForeignKey("users.user_id"))
    fashions = relationship("Fashion", secondary=Fashion_Clothes.__tablename__)
    

class Fashion(Base):
    __tablename__ = "fashions"
    fashion_id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String)
    user_id = Column(String, ForeignKey("users.user_id"))
    clothes = relationship("Clothe", secondary=Fashion_Clothes.__tablename__)
    date = relationship("FashionDate",cascade="all, delete")
    

class FashionDate(Base):
    __tablename__ = "fashion_date"
    date_id = Column(String, primary_key=True, default=generate_uuid)
    date = Column(DateTime, nullable=False)
    fashion_id = Column(String, ForeignKey("fashions.fashion_id"))
    

class Friend(Base):
    __tablename__ = "friends"
    friend_id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False, unique=True)
    tag_color = Column(String, nullable=False)
    user_id = Column(String, ForeignKey("users.user_id"))
    user = relationship("User")
    date = relationship("FriendDate",cascade="all, delete")


class FriendDate(Base):
    __tablename__ = "friend_date"
    date_id = Column(String, primary_key=True, default=generate_uuid)
    date = Column(DateTime, nullable=False)
    friend_id = Column(String, ForeignKey("friends.friend_id"))


