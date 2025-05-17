from pydantic import BaseModel, EmailStr 
from typing import Optional 

class UserBase(BaseModel):
    username:str 
    email:str 

class UserCreate(UserBase):
    password:str 
    
class UserLogin(UserBase):
    username:str 
    password:str
    
class UserUpdate(UserBase):
    username:Optional[str] = None 
    email:Optional[str] = None 
    password:Optional[str] = None 
    
class UserOut(BaseModel):
    id:int 
    username:str 
    email:EmailStr
    role:Optional[str] = None  
    
    class Config:
        orm_mode = True 