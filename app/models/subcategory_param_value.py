from sqlalchemy import Column, String, ForeignKey
from app.database import Base 


class SubcategoryParamValue(Base):
    __tablename__="subcategory_param_values"
    id = Column(String, primary_key=True, index=True)
    subcategory_id = Column(String, ForeignKey("subcategories.id"))
    parameter_id = Column(String, ForeignKey("parameters.id"))
    value = Column(String, nullable=False)