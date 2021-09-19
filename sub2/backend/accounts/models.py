from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.EmailField(max_length=255, unique=True)
    nickname =  models.CharField(max_length=50)
    budget = models.IntegerField()
    travelers = models.IntegerField()
    companion = models.BooleanField()
    transportation = models.CharField(max_length=50)
    selection = models.CharField(max_length=50)
    age = models.IntegerField()
    activity =  models.CharField(max_length=50)
    profile =  models.CharField(max_length=255)
    sex = models.BooleanField(null=True)
    authenticated = models.BooleanField(null=True)

    

    
    
    

    

