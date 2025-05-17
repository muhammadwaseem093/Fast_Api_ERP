from pydantic import BaseModel 

class RolePermissionAssign(BaseModel):
    role_id :int 
    permission_id:int 