from fastapi import APIROuter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.database import SessionLocal 
from app.database import get_db
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

@router.get("/", response_model = list[SubmoduleOut])
def get_submodules(db:Session = Depends(get_db)):
    return  crud_submodule.get_submodules(db)

@router.get("/{module_id}", response_model=SubmoduleOut)
def get_submodule_by_id(submodule_id:int, db:Session = Depends(get_db)):
    submodule = crud_submodule.get_submodule_by_id(db, submodule_id)
    if not submodule:
        raise HTTPException(status_code=400, detail="Subodule Not Found")
    return submodule