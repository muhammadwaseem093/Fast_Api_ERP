from pydantic import BaseModel

class ModuleBase(BaseModel):
    id: str
    name:str
    
class ModuleCreate(ModuleBase):
    pass

class ModuleUpdate(ModuleBase):
    pass

class ModuleOut(ModuleBase):
    class Config:
        orm_mode=True

