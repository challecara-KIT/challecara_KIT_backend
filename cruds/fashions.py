from fastapi import HTTPException
from sqlalchemy.orm.session import Session
from db.model import Fashion, Fashion_Clothes, FashionDate
from schemas.fashions import Fashion as FashionSchema, FashionDate as FashionDateSchema
from db.model import Clothe
from datetime import datetime
from sqlalchemy.sql import func
import time

def get_my_all_fashion(db: Session, user_id: str) -> list[FashionSchema]:
    fashion_orm = db.query(Fashion).filter(Fashion.user_id == user_id).all()
    fashion = list(map(FashionSchema.from_orm, fashion_orm))
    return fashion

def create_fashion(db: Session, user_id: str, clothe_ids: list[str], name:str, date: datetime) -> FashionSchema:
    same_fashion = db.query(Fashion).filter(Fashion.name == name ,Fashion.user_id == user_id).first()
    if same_fashion is None:
        fashion_orm = Fashion(
            user_id=user_id,
            name=name
        )
        db.add(fashion_orm)
        db.commit()
        db.refresh(fashion_orm)
        for clothe_id in clothe_ids:
            clothe = db.query(Clothe).filter(Clothe.clothe_id == clothe_id).first()
            if clothe is None:
                raise HTTPException(status_code=404, detail=f"{clothe_id} clothe not found")
            fashion = Fashion_Clothes(
                fashion_id=fashion_orm.fashion_id,
                clothe_id=clothe_id
            )
            db.add(fashion)
            db.commit()
        fashion_date_orm = FashionDate(
            fashion_id=fashion_orm.fashion_id,
            date=date
        )
        db.add(fashion_date_orm)
        db.commit()
        fashion = FashionSchema.from_orm(fashion_orm)
    else:
        fashion_date_orm = FashionDate(
            fashion_id=same_fashion.fashion_id,
            date=date
        )
        db.add(fashion_date_orm)
        db.commit()
        fashion = FashionSchema.from_orm(same_fashion)
    return fashion

def delete_fashion_by_id(db: Session, fashion_id: str) -> None:
    fashion_orm = db.query(Fashion).filter(Fashion.fashion_id == fashion_id).first()
    if fashion_orm is None:
        raise HTTPException(status_code=404, detail="fashion not found!!")
    db.delete(fashion_orm)
    db.commit()
    return
    

def recommend_fashion_by_date(db: Session, user_id: str) -> list[FashionSchema]:
    fashion_orm = db.query(Fashion).filter(Fashion.user_id == user_id).all()
    fashions: list[FashionSchema] = list(map(FashionSchema.from_orm, fashion_orm))
    recommend = []
    for fashion in fashions:
        date_orm = db.query(FashionDate).filter(FashionDate.fashion_id == fashion.fashion_id).all()
        dates = list(map(FashionDateSchema.from_orm, date_orm))
        recommend.append(max(dates, key=lambda date: date.date))
    sorted(recommend, key=lambda x: x.date)
    recommend = recommend[:3]
    print(f"recommended is {recommend}")
    fashions = []
    for e in recommend:
        fashion = db.query(Fashion).filter(Fashion.fashion_id == e.fashion_id).first()
        fashions.append(FashionSchema.from_orm(fashion))
    return fashions
        
    
            