from sqlalchemy.orm import Session 
from app import models, schemas 


def create_permission(db:Session, permission:schemas.permission.PermissionCreate):
    db_permission = models.permission.Permission(**permission.dict())
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission

def get_permission(db:Session):
    return db.query(models.permission.Permission).all()

def get_permission_by_id(db:Session, permission_id:int):
    return db.query(models.permission.Permission).filter(models.permission.Permission.id == permission_id).first()

def update_permission(db:Session, permission_id:int, permission_update:schemas.permission.PermissionUpdate):
    db_permission = get_permission_by_id(db, permission_id)
    if not db_permission:
        return None 
    if permission_update.name is not None:
         db_permission.name = permission_update.name 
    if permission_update.description is not None:
        db_permission.description = permission_update.description
    db.commit()
    db.refresh(db_permission)
    return db_permission

def delete_permission(db:Session, permission_id:int):
    db_permission = get_permission_by_id(db, permission_id)
    if not db_permission:
        return None 
    db.delete(db_permission)
    db.commit()
    return db_permission