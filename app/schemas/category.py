from pydantic import BaseModel

class CategoryBase(BaseModel):
    id:str
    name:str
    submodule_id:str
    
    
class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    class Config:
        orm_mode = True