from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.database import get_db
from app.schemas.parameter import ParameterCreate, ParameterOut
from app.crud import parameter as crud_parameter

router = APIRouter(prefix="/parameter")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post('/', response_model=ParameterOut)
def create_parameter(parameter:ParameterCreate, db:Session = Depends(get_db)):
    return crud_parameter.create_parameter(db, parameter)

@router.get("/", response_model=list[ParameterOut])
def get_parameters(db:Session = Depends(get_db)):
    return crud_parameter.get_parameters(db)

@router.get('/{parameter_id}', response_model=ParameterOut)
def get_parameter_by_id(parmeter_id:int, db:Session = Depends(get_db)):
    parameter = crud_parameter.get_parameter_by_id(db, parameter_id)
    if not parameter:
        raise HTTPException(status_code=400, detail="Parameter Not Found!")
    return parameter
