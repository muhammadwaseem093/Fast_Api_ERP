from sqlalchemy import Column, String, Integer 
from app.database import Base 

class Permission(Base):
    __tablename__="permissions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=True)
    description = Column(String)