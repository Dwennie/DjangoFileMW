from django.shortcuts import render, redirect, get_object_or_404
from .models import Department


def department_list(request):
    departments = Department.objects.all().order_by("name")
    return render(request, "department/department_list.html", {"departments": departments})


def department_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        department_code = request.POST.get("department_code")
        department_head = request.POST.get("department_head")
        office_location = request.POST.get("office_location")
        founded_date = request.POST.get("founded_date") or None
        Department.objects.create(
            name=name,
            department_code=department_code,
            department_head=department_head,
            office_location=office_location,
            founded_date=founded_date,
        )
        return redirect("department_list")
    return render(request, "department/create_department.html")


def department_edit(request, id):
    department = get_object_or_404(Department, id=id)
    if request.method == "POST":
        department.name = request.POST.get("name")
        department.department_code = request.POST.get("department_code")
        department.department_head = request.POST.get("department_head")
        department.office_location = request.POST.get("office_location")
        department.founded_date = request.POST.get("founded_date") or None
        department.save()
        return redirect("department_list")
    return render(request, "department/create_department.html", {"department": department})


def department_delete(request, id):
    department = get_object_or_404(Department, id=id)
    if request.method == "POST":
        department.delete()
        return redirect("department_list")
    return render(request, "department/delete_department.html", {"department": department})