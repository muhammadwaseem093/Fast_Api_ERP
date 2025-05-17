from sqlalchemy import Column, String, ForeignKey 
from app.database import Base 


class Parameter(Base):
    __tablename__="parameters"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    submodule_id = Column(String, ForeighKey("submodule.id"))
    type=Column(String, default="checkbox")