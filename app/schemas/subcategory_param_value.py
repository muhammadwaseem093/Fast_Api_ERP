from pydantic import BaseModel


class SubcategoryParamValueBase(BaseModel):
    id:str
    subcategory_id:str
    parameter_id:str
    value:str
    
class SubcategoryParamValueCreate(SubcategoryParamValueBase):
    pass
class SubcategoryParamValueUpdate(SubcategoryParamValueBase):
    pass

class SubcategoryParamValueOut(SubcategoryParamValueBase):
    class Config:
        orm_mode = True