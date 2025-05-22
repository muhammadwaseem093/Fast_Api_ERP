from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.database import SessionLocal 
from app.schemas.submodule import SubmoduleCreate, SubmoduleOut
from app.crud import submodule as crud_submodule

router = APIRouter(prefix="/submodules")

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

# ---------------------------- Submodule --------------------------------

@router.post("/", response_model=SubmoduleOut)
def create_submodule(submodule:SubmoduleCreate, db:Session = Depends(get_db)):
    return crud_submodule.create_submodule(db, submodule)

@router.get("/{module_id}", response_model=list[SubmoduleOut])
def get_submodules(module_id:str, db:Session = Depends(get_db)):
    submodule = crud_submodule.get_submodules_by_module(db, module_id)
    if not submodule:
        raise HTTPException(status_code=400, detail="Subodule Not Found")
    return submodule