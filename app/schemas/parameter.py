from pydantic import BaseModel

class ParameterBase(BaseModel):
    id:str
    name:str
    submodule_id:str
    type:str = "checkbox"
    
class ParameterCreate(ParameterBase):
    pass

class ParameterUpdate(ParameterBase):
    pass

class ParameterOut(ParameterBase):
    class Config:
        orm_mode = True