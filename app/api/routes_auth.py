from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.schemas.user import UserCreate, UserOut, UserLogin, UserUpdate
from app.crud import user as crud_user
from app.database import SessionLocal
from app.core.security import create_access_token, verify_password

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users', response_model=list[UserOut])
def list_users(db:Session = Depends(get_db), skip:int = 0, limit:int=100 ):
    return crud_user.get_users(db, skip=skip, limit=limit)


@router.get('/user/{user_id}', response_model=UserOut)
def get_user(user_id:int, db:Session = Depends(get_db)):
    user = crud_user.get_user_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post('/users', response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud_user.create_user(db=db, user=user)
    

@router.put("/user/{user_id}", response_model=UserOut)
def update_user(user_id:int, user_update:UserUpdate, db:Session = Depends(get_db)):
    user = crud_user.update_user(db, user_id=user_id, user_update=user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user 


@router.delete("/user/{user_id}", response_model=UserOut)
def delete_user(user_id:int, db:Session = Depends(get_db)):
    user = crud_user.delete_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user 



@router.post('/signup', response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud_user.create_user(db=db, user=user)


@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud_user.get_user_by_username(db, username=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/logout', status_code=status.HTTP_204_NO_CONTENT)
def logout():
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content={"message": "Logged out successfully"})
    
