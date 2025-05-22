from sqlalchemy import Column, String, ForeignKey
from app.database import Base

class Parameter(Base):
    __tablename__ = "parameters"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, default="checkbox")
    submodule_id = Column(String, ForeignKey("submodules.id"))
    group = Column(String, nullable=False)  # ✅ recently added
