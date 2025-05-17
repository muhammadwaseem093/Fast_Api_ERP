from pydantic import BaseModel
from datetime import date 
from typing import Optional 


class EmployeeBase(BaseModel):
    first_name:str
    last_name:str
    father_name:str
    cnic_number:str
    date_of_birth:Optional[date]
    gender:Optional[str]
    email:Optional[str]
    phone:Optional[str]
    address:Optional[str]
    designation:Optional[str]
    department:Optional[str]
    date_of_joining:Optional[date]
    
class EmployeeCreate(EmployeeBase):
    pass 

class EmployeeUpdate(EmployeeBase):
    pass 

class EmployeeOut(EmployeeBase):
    id:int
    
    
    class Config:
        orm_mode = True 