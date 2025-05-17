from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.orm import Session 
from app.database import SessionLocal 
from app.schemas.role import RoleCreate, RoleOut , RoleUpdate
from app.crud import role as crud_role


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
        
        
@router.post('/roles', response_model=RoleOut)
def create_roles(role:RoleCreate, db:Session = Depends(get_db)):
    return crud_role.create_role(db, role)

@router.get('/roles', response_model = list[RoleOut])
def list_roles(db:Session = Depends(get_db)):
    return crud_role.get_roles(db)   

@router.get('/roles/{role_id}', response_model=RoleOut)
def get_role(role_id:int, db:Session = Depends(get_db)):
    role = crud_role.get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role 

@router.put('/roles/{role_id}', response_model=RoleOut)
def update_role(role_id:int, role_update=RoleUpdate,db: Session = Depends(get_db)):
    updated = crud_role.update_role(db, role_id, role_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Role not found")
    return updated

@router.delete('/roles/{role_id}', response_model=RoleOut)
def delete_role(role_id:int, db:Session = Depends(get_db)):
    deleted = crud_role.delete_role(db, role_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Role not found")
    return deleted