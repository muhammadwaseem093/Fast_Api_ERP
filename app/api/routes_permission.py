from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.orm import Session 
from app.database import SessionLocal 
from app.schemas.permission import PermissionCreate, PermissionOut
from app.crud import permission as role_permission

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
        

@router.post('/create_permission', response_model=PermissionOut)
def create_permission(permission:PermissionCreate, db:Session = Depends(get_db)):
    return role_permission.create_permission(db, permission)

@router.get('/permissions', response_model=list[PermissionOut])
def list_permissions(db:Session = Depends(get_db)):
    return role_permission.get_permission(db)

@router.get('/permissions/{permission_id}', response_model=PermissionOut)
def get_permission(permission_id:int, db:Session = Depends(get_db)):
    permission = role_permission.get_permission_by_id(db, permission_id)
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission

@router.put('/permissions/{permission_id}', response_model=PermissionOut)
def update_permission(permission_id:int, permission_update=PermissionCreate,db: Session = Depends(get_db)):
    updated = role_permission.update_permission(db, permission_id, permission_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Permission not found")
    return updated

@router.delete('/permissions/{permission_id}', response_model=PermissionOut)
def delete_permission(permission_id:int, db:Session = Depends(get_db)):
    deleted = role_permission.delete_permission(db, permission_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Permission not found")
    return deleted