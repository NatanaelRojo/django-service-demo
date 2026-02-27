from django.http import HttpRequest
from ninja import Router

from employees.schemas import EmployeeCreateSchema, EmployeeSchema, EmployeeUpdateSchema
from employees.services import employee_service

router = Router()


@router.get("/employees", response=list[EmployeeSchema])
def get_employees(request: HttpRequest):
    return employee_service.get_all_employees()


def get_employee(employee_id: int):
    return employee_service.get_employee(employee_id)


@router.post("/employees", response=EmployeeSchema)
def create_employee(data: EmployeeCreateSchema):
    return employee_service.create_employee(data)


@router.put("/employees/{employee_id}", response=EmployeeSchema)
def update_employee(employee_id: int, data: EmployeeUpdateSchema):
    return employee_service.update_employee(employee_id, data)


@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    employee_service.delete_employee(employee_id)
    return {"detail": "Employee deleted successfully"}
