from sqlalchemy.orm import Session 
from app.models.subcategory_param_value import SubcategoryParamValue
from app.schemas.subcategory_param_value import SubcategoryParamValueCreate


def create_param_value(db:Session, value:SubcategoryParamValueCreate):
    db_obj = SubcategoryParamValue(**value.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_param_values_by_subcategory(db:Session, subcategory_id:str):
    return db.query(SubcategoryParamValue).filter(SubcategoryParamValue.subcategory_id == subcategory_id).all()