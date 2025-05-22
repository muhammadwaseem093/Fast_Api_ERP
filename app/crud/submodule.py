from sqlalchemy.orm import Session 
from app.models.submodule import Submodule
from app.schemas.submodule import SubmoduleCreate


def create_submodule(db:Session, submodule:SubmoduleCreate):
    db_obj = Submodule(**submodule.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_submodules_by_module(db:Session, module_id:str):
    return db.query(Submodule).filter(Submodule.module_id == module_id).all()

