from django.db import models
from django.forms import CharField

# Create your models here.
class Student(models.Model):
    s_name=models.CharField(max_length=50)
    s_class=models.CharField(max_length=50)
    s_address=models.CharField(max_length=50)
    s_faculty=models.CharField(max_length=50)
    s_mail=models.CharField(max_length=50)
