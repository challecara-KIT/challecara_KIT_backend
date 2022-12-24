from schemas.clothes import Clothe as ClotheSchema
from db.model import Clothe
from sqlalchemy.orm.session import Session
from fastapi import HTTPException


def create_clothe_by_payload(
    db: Session, 
    user_id: str, 
    image_url:str,
    size: str,
    type: str,
    season: str,
    color: str,
) -> ClotheSchema:
    clothe_orm = Clothe(
        image_url=image_url,
        size=size,
        type=type,
        season=season,
        color=color,
        user_id=user_id,
    )
    db.add(clothe_orm)
    db.commit()
    db.refresh(clothe_orm)
    clothe = ClotheSchema.from_orm(clothe_orm)
    return clothe


def delete_clothe_by_id(db: Session, clothe_id: str) -> None:
    clothe = db.query(Clothe).filter(Clothe.clothe_id == clothe_id).first()
    if clothe is None:
        raise HTTPException(status_code=404, detail="clothe not found")
    db.delete(clothe)
    db.commit()
    return


def find_clothe_by_id(db: Session, clothe_id: str) -> ClotheSchema:
    clothe_orm = db.query(Clothe).filter(Clothe.clothe_id == clothe_id).first()
    if clothe_orm is None:
        raise HTTPException(status_code=404, detail="clothe not found")
    clothe = ClotheSchema.from_orm(clothe_orm)
    return clothe