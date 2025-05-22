from sqlalchemy.orm import Session 
from app.models.category import Category
from app.schemas.category import CategoryCreate

def create_category(db:Session, cat:CategoryCreate):
    db_obj = Category(**cat.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_categories_by_submodule(db:Session, submodule_id:str):
    return db.query(Category).filter(Category.submodule_id == submodule_id).all()