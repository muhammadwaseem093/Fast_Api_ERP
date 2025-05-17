from fastapi import APIRouter
from app.api import routes_auth, routes_roles, routes_permission , routes_role_permission, routes_employee

api_router = APIRouter()

api_router.include_router(routes_auth.router, tags=["Auth"])
api_router.include_router(routes_roles.router, tags=["Roles"])
api_router.include_router(routes_permission.router, tags=["Permissions"])
api_router.include_router(routes_role_permission.router, tags=["Role Permission"])
api_router.include_router(routes_employee.router, tags=["Employee"])