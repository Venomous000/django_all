from django.contrib import admin
from home.models import *
# Register your models here.

@admin.register(Car)
class Car_Admin(admin.ModelAdmin):
    list_display = ('car_name', 'speed')
    search_fields = ('car_name'),

@admin.register(Student)
class Student_Admin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'address', 'image', 'file') 
    search_fields = ('name', 'email')