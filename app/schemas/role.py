from pydantic import BaseModel 
from typing import Optional 


class RoleBase(BaseModel):
    name:str 
    description:str 
    
class RoleCreate(RoleBase):
    pass 

class RoleUpdate(RoleBase):
    name:Optional[str] = None 
    description:Optional[str] = None
    
class RoleOut(RoleBase):
    id:int 
    class Config:
        orm_mode = True 