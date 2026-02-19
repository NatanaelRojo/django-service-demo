from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST

from employees.dtos.employee_dto import EmployeeDTO, UpdateEmployeeDTO
from employees.models.employee import Employee
from employees.requests.create_employee import CreateEmployeeRequest
from employees.requests.update_employee import UpdateEmployeeRequest
from employees.services import employee_service


def index(request):
    employees = employee_service.get_all_employees()
    context = {"employees": employees}
    return render(request, "employees/index.html", context)


@require_GET
def create(request: HttpRequest) -> HttpResponse:
    return render(request, "employees/create_employee.html")


def edit(request, employee_id):
    employee = employee_service.get_employee(employee_id)
    context = {"employee": employee}
    return render(request, "employees/update.html", context)


@require_POST
def store(request: HttpRequest) -> HttpResponse:
    form = CreateEmployeeRequest(request.POST)

    if not form.is_valid():
        return HttpResponse(f"Invalid data: {form.errors}", status=400)

    employee_dto = EmployeeDTO(**form.cleaned_data)
    employee_service.create_employee(employee_dto)
    return redirect(reverse("employees:index"))


def delete(request: HttpRequest, employee_id: int) -> HttpResponse:
    employee_service.delete_employee(employee_id)
    return redirect(reverse("employees:index"))


def update(request: HttpRequest, employee_id: int) -> HttpResponse:
    employee_data = UpdateEmployeeRequest(request.POST)
    if not employee_data.is_valid():
        return HttpResponse(f"Invalid data: {employee_data.errors}", status=400)

    employee_dto = UpdateEmployeeDTO(**employee_data.cleaned_data)
    employee_service.update_employee(employee_id, employee_dto)
    return redirect(reverse("employees:index"))
