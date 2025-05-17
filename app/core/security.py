from datetime import datetime, timedelta 
from typing import Optional 
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.core.config import settings 


pwd_context= CryptContext(schemes=['bcrypt'], deprecated="auto")

# hash password 
def hash_password(password:str) -> str:
    return pwd_context.hash(password)

# verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# create access token 
def create_access_token(data:dict, expire_delta:Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expire_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


# decode access token
def decode_access_token(token:str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload 
    except JWTError:
        return None 