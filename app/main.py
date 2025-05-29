from fastapi import FastAPI
from app.api import api_router
from app.database import Base, engine 
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app =FastAPI(title="RBAC API")

origin = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)