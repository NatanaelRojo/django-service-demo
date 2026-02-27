from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from employees.dtos.employee_dto import UpdateEmployeeDTO
from employees.models.employee import Employee
from employees.schemas import EmployeeCreateSchema, EmployeeUpdateSchema


@transaction.atomic
def create_employee(data: EmployeeCreateSchema) -> Employee:
    User = get_user_model()
    user = User.objects.create_user(
        username=data.username,
        first_name=data.first_name,
        last_name=data.last_name,
        password=data.password,
    )
    employee = Employee.objects.create(
        user=user,
        id_number=data.id_number,
        position=data.position,
        department=data.department,
    )
    return employee


@transaction.atomic
def update_employee(employee_id: int, data: EmployeeUpdateSchema) -> Employee:
    employee = get_object_or_404(Employee, id=employee_id)
    user = employee.user
    user_fields = [
        "username",
        "first_name",
        "last_name",
    ]
    employee_fields = ["id_number", "position", "department"]
    for field, value in data.dict(exclude_unset=True).items():
        if field in user_fields:
            setattr(user, field, value)
        elif field in employee_fields:
            setattr(employee, field, value)
    if data.password is not None and data.password != "":
        user.set_password(data.password)
    user.save()
    employee.save()
    return employee


def delete_employee(employee_id: int) -> None:
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()


def get_all_employees() -> QuerySet[Employee]:
    return Employee.objects.select_related("user").all()


def get_employee(employee_id: int) -> Employee:
    return get_object_or_404(Employee, id=employee_id)
