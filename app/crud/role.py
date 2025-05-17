from sqlalchemy.orm import Session 
from app import models, schemas 

def create_role(db:Session, role:schemas.role.RoleCreate):
    db_role = models.role.Role(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role 

# Get all roles
def get_roles(db:Session):
    return db.query(models.role.Role).all()

# get role by id 
def get_role_by_id(db:Session, role_id:int):
    return db.query(models.role.Role).filter(models.role.Role.id == role_id).first()


# update role 
def update_role(db:Session, role_id:int, role_update:schemas.role.RoleUpdate):
    db_role = get_role_by_id(db, role_id)
    if not db_role:
        return None 
    if role_update.name is not None:
         db_role.name = role_update.name 
    if role_update.description is not None:
        db_role.description = role_update.description
    db.commit()
    db.refresh(db_role)
    return db_role
def delete_role(db:Session, role_id:int):
    db_role = get_role_by_id(db, role_id)
    if not db_role:
        return None 
    db.delete(db_role)
    db.commit()
    return db_role 