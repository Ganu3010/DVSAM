from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class UserData(AbstractUser):
    res1 = models.CharField(max_length=20)
    rate1 = models.IntegerField(blank=True, null=True)
    res2 = models.CharField(max_length=20)
    rate2 = models.IntegerField(blank=True, null=True)
    res3 = models.CharField(max_length=20)
    rate3 = models.IntegerField(blank=True, null=True)
    res4 = models.CharField(max_length=20)
    rate4 = models.IntegerField(blank=True, null=True)
    res5 = models.CharField(max_length=20)
    rate5 = models.IntegerField(blank=True, null=True)
    i = models.IntegerField(blank=True, null=True)
   