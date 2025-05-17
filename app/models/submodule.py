from sqlalchemy import Column, String, ForeignKey
from app.database import Base 

class Submodule(Base):
    __tablename__="submodules"
    id = Column(String, primary_key=True, index=True)
    name=Column(String, nullable=False)
    module_id = Column(String, ForeignKey("modules.id", , ondelete="CASCADE"))