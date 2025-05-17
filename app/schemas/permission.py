from pydantic import BaseModel 
from typing import Optional 


class PermissionBase(BaseModel):
    name:str 
    description:str 
    
class PermissionCreate(PermissionBase):
    pass 

class PermissionUpdate(PermissionBase):
    name:Optional[str] = None 
    description:Optional[str] = None


class PermissionOut(PermissionBase):
    id:int 
    class Config:
        orm_mode = True 