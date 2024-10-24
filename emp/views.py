from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee

# Create your views here.
def allemployees(request):
    emp = Employee.objects.all()
    return render(request, "emp/allemployees.html", {"allemployees":emp})


def singleemployee(request, empid):
    return render(request, "emp/singleemployee.html")


def addemployee(request):
    if request.method == "POST":
    # Take all the parameters from the form 
        employeeid = request.POST.get('employeeid')
        employeename = request.POST.get('employeename')
        email = request.POST.get('email')
        cellphone = request.POST.get('cellphone')
        address = request.POST.get('address')

        # create an object of the employee model
        e = Employee()
        e.employeeid = employeeid
        e.employeename = employeename
        e.email = email
        e.phone = cellphone
        e.address = address
        e.save()
        return redirect("/allemployees")

    return render(request, "emp/addemployee.html")

def deleteemployee(request, empid):
    e = Employee.objects.get(pk = empid)
    e.delete()
    return redirect("allemployees")

def updateemployee(request, empid):
    e = Employee.objects.get(pk = empid)

    return render(request, "emp/updateemployee.html", {"singleemp": e})

def doupdateemployee(request, empid):
    updateemployeeid = request.POST.get('employeeid')
    updateemployeename = request.POST.get('employeename')
    updateemployeeemail = request.POST.get('email')
    updateemployeephone = request.POST.get('cellphone')
    updateemployeeaddress = request.POST.get('address')

    emp = Employee.objects.get(pk = empid)

    emp.employeeid = updateemployeeid
    emp.employeename = updateemployeename
    emp.email = updateemployeeemail
    emp.address = updateemployeeaddress
    emp.phone = updateemployeephone
    emp.save()
    return redirect("allemployees")