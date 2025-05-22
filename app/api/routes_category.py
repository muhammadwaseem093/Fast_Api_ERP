from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.category import CategoryCreate, CategoryOut
from app.crud import category as crud_category

router = APIRouter(prefix="/category")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post('/', response_model=CategoryOut)
def create_category(category:CategoryCreate, db:Session = Depends(get_db)):
    return crud_category.create_category(db, category)


@router.get('/{submodule_id}', response_model=list[CategoryOut])
def get_categories(submodule_id:str, db:Session = Depends(get_db)):
    return crud_category.get_categories_by_submodule(db, submodule_id)
