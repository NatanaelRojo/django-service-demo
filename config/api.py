from ninja import NinjaAPI

from employees.api import router as employee_router

api = NinjaAPI(
    title="Employee Onboarding API",
    version="1.0",
    description="API for managing employee onboarding processes.",
)

api.add_router("/employees", employee_router)
