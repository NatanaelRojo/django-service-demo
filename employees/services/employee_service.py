from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404

from employees.dtos.employee_dto import EmployeeDTO, UpdateEmployeeDTO
from employees.models.employee import Employee


@transaction.atomic
def create_employee(employee_dto: EmployeeDTO) -> Employee:
    User = get_user_model()
    user = User.objects.create_user(
        username=employee_dto.username,
        first_name=employee_dto.first_name,
        last_name=employee_dto.last_name,
        password=employee_dto.password,
    )
    employee = Employee.objects.create(
        user=user,
        id_number=employee_dto.id_number,
        position=employee_dto.position,
        department=employee_dto.department,
    )
    return employee


@transaction.atomic
def update_employee(employee_id: int, employee_dto: UpdateEmployeeDTO) -> Employee:
    employee = get_object_or_404(Employee, id=employee_id)
    user = employee.user
    user_fields = [
        "username",
        "first_name",
        "last_name",
    ]
    employee_fields = ["id_number", "position", "department"]

    for field in user_fields:
        value = getattr(employee_dto, field, None)
        if value is not None and value != "":
            setattr(user, field, value)
    if employee_dto.password is not None and employee_dto.password != "":
        user.set_password(employee_dto.password)
    user.save()

    for field in employee_fields:
        value = getattr(employee_dto, field, None)
        if value is not None and value != "":
            setattr(employee, field, value)
    employee.save()
    return employee


def delete_employee(employee_id: int) -> None:
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()


def get_all_employees() -> list[Employee]:
    return Employee.objects.select_related("user").all()


def get_employee(employee_id: int) -> Employee:
    return get_object_or_404(Employee, id=employee_id)
