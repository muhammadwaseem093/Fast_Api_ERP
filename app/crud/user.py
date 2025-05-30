from sqlalchemy.orm import Session 
from fastapi.responses import JSONResponse
from app import models, schemas
from app.core.security import hash_password,verify_password 


# get user by username 
def get_user_by_username(db:Session, username:str):
    return db.query(models.user.User).filter(models.user.User.username == username).first()

def get_user_by_id(db:Session, user_id:int):
    return db.query(models.user.User).filter(models.user.User.id == user_id).first()

def get_users(db:Session, skip:int=0, limit:int = 100):
    return db.query(models.user.User).offset(skip).limit(limit).all()

def create_user(db:Session, user:schemas.user.UserCreate):
    db_user = models.user.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
        is_active=user.is_active,
        role_id=user.role_id,
        
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user 


def update_user(db:Session, user_id:int, user_update:schemas.user.UserUpdate):
    db_user = db.query(models.user.User).filter(models.user.User.id == user_id).first()
    if not db_user:
        return None 
    
    if user_update.username:
        db_user.username = user_update.username 
    if user_update.email:
        db_user.email = user_update.email 
    if user_update.password:
        db_user.hashed_password = hash_password(user_update.password)
        
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db:Session, user_id:int):
    db_user  = db.query(models.user.User),filter(models.user.User.id == user_id).first()
    if not db_user:
        return None 
        
    db.delete(db_user)
    db.commit()
    return db_user 