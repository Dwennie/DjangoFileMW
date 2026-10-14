from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name", "department_code", "department_head", "office_location", "founded_date"]
        widgets = {
            "founded_date": forms.DateInput(attrs={"type": "date"}),
        }

