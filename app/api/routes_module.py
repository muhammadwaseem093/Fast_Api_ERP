from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.database import SessionLocal 
from app.schemas.module import ModuleCreate, ModuleOut
from app.crud import module as crud_module

router = APIRouter(prefix="/modules")

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

# ---------------------------- Module Operations --------------------------------

@router.post("/", response_model=ModuleOut)
def create_module(module: ModuleCreate, db: Session = Depends(get_db)):
    return crud_module.create_module(db, module)

@router.get("/", response_model=list[ModuleOut])
def get_modules(db: Session = Depends(get_db)):
    return crud_module.get_modules(db)

@router.get("/{module_id}", response_model=ModuleOut)
def get_module_by_id(module_id: str, db: Session = Depends(get_db)):
    module = crud_module.get_module_by_id(db, module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Module Not Found")
    return module

@router.put("/{module_id}", response_model=ModuleOut)
def update_module(module_id: str, updated_module: ModuleCreate, db: Session = Depends(get_db)):
    module = crud_module.get_module_by_id(db, module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Module Not Found")

    return crud_module.update_module(db, module_id, updated_module)

@router.delete("/{module_id}")
def delete_module(module_id: str, db: Session = Depends(get_db)):
    module = crud_module.get_module_by_id(db, module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Module Not Found")

    crud_module.delete_module(db, module_id)
    return {"message": "Module deleted successfully"}
