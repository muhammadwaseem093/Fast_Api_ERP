from sqlalchemy import Column, String, ForeignKey
from app.database import Base 

class Subcategory(Base):
    __tablename__ = "subcategories"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category_id = Column(String, ForeignKey("categories.id"))