from pydantic import BaseModel


class SubmoduleBase(BaseModel):
    id:str
    name:str
    module_id:str
    
class SubmoduleCreate(SubmoduleBase):
    pass

class SubmoduleUpdate(SubmoduleBase):
    pass

class SubmoduleOut(SubmoduleBase):
    class Config:
        orm_mode = True