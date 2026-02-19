from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django import forms

from employees.models.employee import Employee


class UpdateEmployeeRequest(forms.Form):
    id_number = forms.CharField(max_length=20, required=False)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    position = forms.CharField(max_length=100, required=False)
    department = forms.CharField(max_length=100, required=False)
    username = forms.CharField(max_length=150, required=False)
    password = forms.CharField(validators=[MinLengthValidator(8)], required=False)

    def clean_username(self) -> str:
        username = self.cleaned_data.get("username")
        User = get_user_model()
        user_already_exists = User.objects.filter(username=username).exists()
        if username and user_already_exists:
            raise forms.ValidationError("Username already exists.")
        return username

    def clean_id_number(self) -> str:
        id_number = self.cleaned_data.get("id_number")
        employee_already_exists = Employee.objects.filter(id_number=id_number).exists()
        if id_number and employee_already_exists:
            raise forms.ValidationError("ID number already exists.")
        return id_number
