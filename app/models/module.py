from sqlalchemy import Column, String 
from app.database import Base 


class Module(Base):
    __tablename__="modules"
    id = Column(String, primary_key=True, index=True)
    name = Column(string, nullable=False)