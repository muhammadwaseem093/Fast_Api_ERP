from sqlalchemy import Column, Integer, String, Date
from app.database import Base 


class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    father_name = Column(String, nullable=False)
    cnic_number = Column(String, unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    designation = Column(String, nullable=False)
    department = Column(String, nullable=False)
    date_of_joining = Column(Date, nullable=False)
    