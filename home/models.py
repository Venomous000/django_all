from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null = True, blank = True)
    image = models.ImageField()
    file = models.FileField()

class Product(models.Model):
    pass

class Car(models.Model):
    car_name = models.CharField(max_length = 50)
    speed = models.IntegerField(default = 50)

    def __str__(self):
        return self.car_name