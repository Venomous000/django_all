from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def home(request):
#     return render(request, "")
from home.models import *

def home_view(request):
    cars = Car.objects.all()
    students = Student.objects.all()
    return render(request, 'home/index.html', {'cars': cars, 'students': students})
