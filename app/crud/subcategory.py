from sqlalchemy.orm import Session 
from app.models.subcategory import Subcategory
from app.schemas.subcategory import SubcategoryCreate


def create_subcategory(db:Session, subcat:SubcategoryCreate):
    db_obj = Subcategory(**subcat.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_subcategories_by_category(db:Session, category_id:str):
    return sb:query(Subcategory).filter(Subcategory.category_id = category_id).all