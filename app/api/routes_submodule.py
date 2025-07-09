from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.database import SessionLocal 
from app.schemas.submodule import SubmoduleCreate, SubmoduleOut, SubmoduleUpdate
from app.crud import submodule as crud_submodule

router = APIRouter(prefix="/submodules")

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

# ---------------------------- Submodule Routes --------------------------------

@router.post("/", response_model=SubmoduleOut)
def create_submodule(submodule: SubmoduleCreate, db: Session = Depends(get_db)):
    return crud_submodule.create_submodule(db, submodule)


@router.get("/{module_id}", response_model=list[SubmoduleOut])
def get_submodules(module_id: str, db: Session = Depends(get_db)):
    return crud_submodule.get_submodules_by_module(db, module_id)


@router.get("/detail/{submodule_id}", response_model=SubmoduleOut)
def get_submodule(submodule_id: str, db: Session = Depends(get_db)):
    submodule = crud_submodule.get_submodule_by_id(db, submodule_id)
    if not submodule:
        raise HTTPException(status_code=404, detail="Submodule not found")
    return submodule


@router.put("/{submodule_id}", response_model=SubmoduleOut)
def update_submodule(submodule_id: str, submodule_data: SubmoduleUpdate, db: Session = Depends(get_db)):
    updated = crud_submodule.update_submodule(db, submodule_id, submodule_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Submodule not found")
    return updated


@router.delete("/{submodule_id}")
def delete_submodule(submodule_id: str, db: Session = Depends(get_db)):
    deleted = crud_submodule.delete_submodule(db, submodule_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Submodule not found")
    return {"success": True, "message": "Submodule deleted"}
