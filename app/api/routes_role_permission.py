from fastapi import APIRouter, Depends 
from sqlalchemy.orm import Session 
from app.database import SessionLocal 
from app.schemas.role_permission import RolePermissionAssign 
from app.crud import role_permission as crud_role_permission


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
        
        
@router.post("/assign_permission_to_role")
def assign_permission(payload:RolePermissionAssign, db:Session =Depends(get_db)):
    return crud_role_permission.assign_permission_to_role(db, role_id=payload.role_id, permission_id=payload.permission_id)