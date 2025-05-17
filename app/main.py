from fastapi import FastAPI
from app.api import api_router
from app.database import Base, engine 

Base.metadata.create_all(bind=engine)

app =FastAPI(title="RBAC API")


app.include_router(api_router)