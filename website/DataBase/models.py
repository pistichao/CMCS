from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    cars = models.CharField(max_length=100)


class Cars(models.Model):
    carname = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    tasks = models.CharField(max_length=100)


class Tasks(models.Model):
    taskname = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    status = models.CharField(max_length=100)