from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base 

class RolePermission(Base):
    __tablename__ ="role_permissions"
    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"))
    permission_id = Column(Integer, ForeignKey("permissions.id", ondelete="CASCADE"))