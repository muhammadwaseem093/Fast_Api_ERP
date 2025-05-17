from sqlalchemy.orm import Session
from app.models.module import Module
from app.schemas.module import ModuleCreate


def create_module(db:Session, module:ModuleCreate):
    db_obj = Module(**module.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db.obj)
    return db_obj

def get_modules(db:Session):
    return db.query(Module).all()

def get_module_by_id(db:Session, module_id:Str):
    return db.query(Module).filter(Module.id == module_id).first()