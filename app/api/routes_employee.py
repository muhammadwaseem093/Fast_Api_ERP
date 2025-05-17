from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.orm import Session 
from app.database import SessionLocal 
from app.schemas.employee import EmployeeCreate, EmployeeUpdate,EmployeeOut
from app.crud import employee as employee_crud


router = APIRouter(prefix="/employees")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post('/', response_model=EmployeeOut)
def create_employee(employee:EmployeeCreate, db:Session = Depends(get_db)):
    return employee_crud.create_employee(db, employee)


@router.get('/', response_model = list[EmployeeOut])
def list_employees(db:Session = Depends(get_db)):
    return employee_crud.get_employees(db)

@router.get('/{employee_id}', response_model=EmployeeOut)
def get_employee(employee_id:int, db:Session = Depends(get_db)):
    employee = employee_crud.get_employee_by_id(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee Not Found!")
    return employee

@router.put('/{employee_id}', response_model=EmployeeOut)
def update_employee(employee_id:int, employee_update:EmployeeUpdate, db:Session = Depends(get_db)):
    updated = employee_crud.update_employee(db, employee_id, employee_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee Not Found!")
    return updated


@router.delete("/{employee_id}", response_model=EmployeeOut)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    try:
        deleted = employee_crud.delete_employee(db, employee_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Employee Not Found!")
        return deleted
    except Exception as e:
        print(f"Error while deleting employee {employee_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    