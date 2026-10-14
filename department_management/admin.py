from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_code", "name", "department_head", "office_location", "founded_date", "created_at")
    search_fields = ("name", "department_code", "department_head", "office_location")
    ordering = ("department_code",)