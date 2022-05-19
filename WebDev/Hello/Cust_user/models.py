from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class UserData(AbstractUser):
    res1 = models.CharField(max_length=20, blank=True)
    rate1 = models.IntegerField(default=-1)
    res2 = models.CharField(max_length=20, blank=True)
    rate2 = models.IntegerField(default=-1)
    res3 = models.CharField(max_length=20, blank=True)
    rate3 = models.IntegerField(default=-1)
    res4 = models.CharField(max_length=20, blank=True)
    rate4 = models.IntegerField(default=-1)
    res5 = models.CharField(max_length=20, blank=True)
    rate5 = models.IntegerField(default=-1)
    i = models.IntegerField(default=0)
   