from sqlalchemy.orm import Session
from app.models.employee import Employee 
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeOut

def create_employee(db:Session, employee: EmployeeCreate):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# get employee by id
def get_employee_by_id(db:Session, employee_id:int):
    return db.query(Employee).filter(Employee.id == employee_id).first()

# get employees 
def get_employees(db:Session, skip:int = 0, limit:int = 100):
    return db.query(Employee).offset(skip).limit(limit).all()

#update employee
def update_employee(db:Session, employee_id:int, employee_data:EmployeeUpdate):
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return None 
    for key, value in employee_data.dict(exclude_unset=True).items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee


# delete employee
def delete_employee(db: Session, employee_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return None
    db.delete(employee)
    db.commit()
    return employee
