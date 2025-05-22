from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.subcategory import SubcategoryCreate, SubcategoryOut
from app.crud import subcategory as crud_subcategory

router = APIRouter(prefix="/sub-category")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post('/', response_model=SubcategoryOut)
def create_subcategory(subcategory:SubcategoryCreate, db:Session = Depends(get_db)):
    return crud_subcategory.create_subcategory(db, subcategory)

@router.get('/{category_id}', response_model=list[SubcategoryOut])
def get_subcategories(category_id:str, db:Session = Depends(get_db)):
    return crud_subcategory.get_subcategories_by_category(db, category_id)
