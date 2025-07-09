from pydantic import BaseModel

class SubmoduleBase(BaseModel):
    name: str
    module_id: str

class SubmoduleCreate(SubmoduleBase):
    id: str

class SubmoduleUpdate(BaseModel):
    name: str | None = None

class SubmoduleOut(SubmoduleBase):
    id: str

    class Config:
        orm_mode = True
