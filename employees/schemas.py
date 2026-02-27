from typing import Optional

from django.contrib.auth import get_user_model
from ninja import ModelSchema, Schema

from employees.models.employee import Employee


class UserSchema(ModelSchema):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
        ]


class EmployeeSchema(ModelSchema):
    class Meta:
        model = Employee
        fields = [
            "id_number",
            "position",
            "department",
        ]

    user: UserSchema


class EmployeeCreateSchema(Schema):
    first_name: str
    last_name: str
    username: str
    password: str
    id_number: str
    position: str
    department: str


class EmployeeUpdateSchema(Schema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    id_number: Optional[str] = None
    position: Optional[str] = None
    department: Optional[str] = None
