from django.db.models import fields
from rest_framework import serializers
from accounts.models import *
from .models import *

class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToruistImg
        fields = ('images',)


class tourSerializer(serializers.ModelSerializer):
    img = imageSerializer(many=True,read_only=True)
    class Meta:
        model = Touristspot

        fields =('id','title','category','categorydetail','latitude','longitude','address','code','counting','img')


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname',)
    
class reviewSerializer(serializers.ModelSerializer):
    user = UserNameSerializer()
    class Meta:
        model = Review
        fields = ('rating','content','created_at','user')

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'
    
class RouteTouristspotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route_Touristspot()
        fields = '__all__'