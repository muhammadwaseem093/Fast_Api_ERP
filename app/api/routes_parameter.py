from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
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


@router.get('/{submodule_id}', response_model=list[ParameterOut])
def get_parameters(submodule_id:str, db:Session = Depends(get_db)):
    return crud_parameter.get_parameters_by_submodule(db, submodule_id)
