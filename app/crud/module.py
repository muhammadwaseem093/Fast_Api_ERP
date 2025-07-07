from sqlalchemy.orm import Session
from app.models.module import Module
from app.schemas.module import ModuleCreate


def create_module(db: Session, module: ModuleCreate):
    db_obj = Module(**module.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_modules(db: Session):
    return db.query(Module).all()

def get_module_by_id(db: Session, module_id: str):
    return db.query(Module).filter(Module.id == module_id).first()

def update_module(db: Session, module_id: str, updated_data: ModuleCreate):
    db_obj = get_module_by_id(db, module_id)
    if not db_obj:
        return None

    db_obj.name = updated_data.name  # Update allowed fields only
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_module(db: Session, module_id: str):
    db_obj = get_module_by_id(db, module_id)
    if not db_obj:
        return False

    db.delete(db_obj)
    db.commit()
    return True
