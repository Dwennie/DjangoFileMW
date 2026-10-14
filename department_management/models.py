from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    department_code = models.CharField(max_length=10, unique=True)
    department_head = models.CharField(max_length=100, blank=True, null=True)
    office_location = models.CharField(max_length=200, blank=True, null=True)
    founded_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.department_code} - {self.name}"
