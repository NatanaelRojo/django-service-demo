from django.urls import path

from employees.controllers import employee_controller
from employees.controllers.employee_controller import (
    index,
    create,
    edit,
    store,
    delete,
    update,
)

app_name = "employees"
urlpatterns = [
    path("", index, name="index"),
    path("create/", create, name="create"),
    path("store/", store, name="store"),
    path("edit/<int:employee_id>/", edit, name="edit"),
    path("delete/<int:employee_id>/", delete, name="delete"),
    path("update/<int:employee_id>/", update, name="update"),
]
