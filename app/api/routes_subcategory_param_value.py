from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.subcategory_param_value import SubcategoryParamValueCreate, SubcategoryParamValueOut
from app.crud import subcategory_param_value as crud_subcategory_param

router = APIRouter(prefix="/subcategory-param")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post('/', response_model=SubcategoryParamValueOut)
def create_param_value(subcatparam:SubcategoryParamValueCreate, db:Session = Depends(get_db)):
    return crud_subcategory_param.create_param_value(db, subcatparam)

@router.get('/{subcategory_id}', response_model=list[SubcategoryParamValueOut])
def get_param_values(subcategory_id:str, db:Session = Depends(get_db)):
    return crud_subcategory_param.get_param_values_by_subcategory(db, subcategory_id)
