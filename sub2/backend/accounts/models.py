from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from tour.models import *

class User(AbstractUser):
    username = models.EmailField(max_length=255, unique=True)
    nickname =  models.CharField(max_length=50, unique=True)
    budget = models.IntegerField(null=True)
    travelers = models.IntegerField(null=True)
    companion = models.BooleanField(null=True)
    transportation = models.CharField(max_length=50,null=True)
    selection = models.CharField(max_length=50,null=True)
    age = models.IntegerField(null=True)
    activity =  models.CharField(max_length=50,null=True)
    profile =  models.CharField(max_length=255,null=True)
    sex = models.BooleanField(null=True)
    authenticated = models.BooleanField(null=True)

class City(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True)
    state = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    satis = models.FloatField()
    code = models.IntegerField()    

class WishList(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Touristspot = models.ForeignKey(Touristspot, on_delete=models.CASCADE)

    
    
    

    

