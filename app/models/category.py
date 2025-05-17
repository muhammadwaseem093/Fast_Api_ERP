from sqlalchemy import Column , String, ForeighKey
from app.database import Base 

class Category(Base):
    __tablename__="categories"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    submodule_id = Column(String, ForeignKey("submodules.id"))
    