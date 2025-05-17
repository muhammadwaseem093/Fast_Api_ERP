from sqlalchemy.orm import Session 
from app.models.parameter import Parameter
from app.schemas.parameter import ParameterCreate


def create_parameter(db:Session, param:ParameterCreate):
    db_obj = Parameter(**param.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_parameters_by_submodule(db:Session, submodule_id:str):
    return db.query(Parameter).filter(Parameter.submodule_id == submodule_id).all()