from sqlalchemy.orm import Session 
from app import models, schemas 


def  assign_permission_to_role(db:Session, role_id:int, permission_id:int):
    # check if the permission is already asin
    existing = db.query(models.role_permission.RolePermission).filter_by(role_id=role_id, permission_id=permission_id).first()
    if existing:
        return {"message": "Permission already assigned to role"}
    
    role_permission = models.role_permission.RolePermission(role_id=role_id, permission_id=permission_id)
    db.add(role_permission)
    db.commit()
    db.refresh(role_permission)
    return {"message": "Permission assigned to role successfully", "role_permission": role_permission }