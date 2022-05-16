from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    msg = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name




  


    