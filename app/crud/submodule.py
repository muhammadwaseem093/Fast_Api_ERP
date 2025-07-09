from sqlalchemy.orm import Session
from app.models.submodule import Submodule
from app.schemas.submodule import SubmoduleCreate, SubmoduleUpdate


def create_submodule(db: Session, submodule: SubmoduleCreate):
    db_obj = Submodule(**submodule.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_submodules_by_module(db: Session, module_id: str):
    return db.query(Submodule).filter(Submodule.module_id == module_id).all()


def get_submodule_by_id(db: Session, submodule_id: str):
    return db.query(Submodule).filter(Submodule.id == submodule_id).first()


def update_submodule(db: Session, submodule_id: str, update_data: SubmoduleUpdate):
    submodule = get_submodule_by_id(db, submodule_id)
    if not submodule:
        return None
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(submodule, field, value)
    db.commit()
    db.refresh(submodule)
    return submodule


def delete_submodule(db: Session, submodule_id: str):
    submodule = get_submodule_by_id(db, submodule_id)
    if not submodule:
        return None
    db.delete(submodule)
    db.commit()
    return submodule
