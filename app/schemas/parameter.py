from pydantic import BaseModel

class ParameterBase(BaseModel):
    id:str
    name:str
    type:str = "checkbox"
    submodule_id:str
    group:str

    
class ParameterCreate(ParameterBase):
    pass

class ParameterUpdate(ParameterBase):
    pass

class ParameterOut(ParameterBase):
    class Config:
        orm_mode = True