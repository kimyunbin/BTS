from django.conf import settings
from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
class Touristspot(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=125)
    category = models.CharField(max_length=50)
    categorydetail = models.CharField(max_length=125)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=125)
    code = models.IntegerField()
    counting = models.IntegerField(default=0)


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Touristspot = models.ForeignKey(Touristspot, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField()

class ToruistImg(models.Model):
    id = models.AutoField(primary_key=True)
    Touristspot = models.ForeignKey(Touristspot,on_delete=models.CASCADE,related_name='img')
    images = models.TextField()
