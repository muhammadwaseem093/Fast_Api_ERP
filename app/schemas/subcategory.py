from pydantic import BaseModel


class SubcategoryBase(BaseModel):
    id:str
    name:str
    category_id:str
    
    
class SubcategoryCreate(SubcategoryBase):
    pass

class SubcategoryUpdate(SubcategoryBase):
    pass

class SubcategoryOut(SubcategoryBase):
    class Config:
        orm_mode= True