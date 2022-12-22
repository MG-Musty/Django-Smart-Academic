from django.db import models
from django.contrib.auth.models import AbstractUser
from tkinter import CASCADE

#from . import views
# Create your models here.
#from users.models import Teacher
#from .forms import TeacherForm
class User(AbstractUser):
    pass


class Teacher(models.Model):
    firstname = models.fields.CharField(max_length=50)
    surname = models.fields.CharField(max_length=50)
    mobile = models.fields.CharField(max_length=16)
    email = models.fields.CharField(max_length=200)
    location = models.fields.CharField(max_length=100)
    position = models.fields.CharField(max_length=100)

    def __str__(self):
        return self.firstname