from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from main_app.app_forms import EmployeeForm
from main_app.models import Employee


# Create your views here.
def home(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = EmployeeForm()
    return render(request, "employee.html", {"form": form})


def all_employees(request):
    employees = Employee.objects.all()
    # employees = Employee.objects.all().order_by("-salary")
    # employees = Employee.objects.filter(name__istartswith="mi").order_by("-dob")
    # today = datetime.today()
    # day = today.day
    # month = today.month
    # employees = Employee.objects.filter(Q(name__contains="la") | Q(salary__gt=70000))
    #employees = Employee.objects.filter(dob__day=day, dob__month=month)
    return render(request, "all_employees.html", {"employees": employees})


def employee_details(request, emp_id):
    employee = Employee.objects.get(pk=emp_id)
    return render(request, "employee_details.html", {"employee": employee})


def employee_delete(request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    employee.delete()
    return redirect("all")
