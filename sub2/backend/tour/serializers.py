from django.db.models import fields
from rest_framework import serializers
from accounts.models import *
from .models import *
from django.db.models import Avg, F
class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToruistImg
        fields = ('awsimages',)



class tourSerializer(serializers.ModelSerializer):
    img = imageSerializer(many=True,read_only=True)
    avg_rating = serializers.SerializerMethodField('get_avg_rating',read_only =True)

    class Meta:
        model = Touristspot

        fields =('id','title','category','categorydetail','latitude','longitude','address','code','counting','img','avg_rating')

    def get_avg_rating(self,obj):
        # for particular musician get all albums and aggregate the all stars and return the avg_rating
        return Review.objects.filter(Touristspot = obj.id).aggregate(Avg('rating'))['rating__avg']

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname',)
    
class reviewSerializer(serializers.ModelSerializer):
    user = UserNameSerializer()
    class Meta:
        model = Review
        fields = ('rating','content','created_at','user')


class RouteTouristspotSerializer(serializers.ModelSerializer):
    touristspot = tourSerializer(read_only=True)
    class Meta:
        model = RouteTouristspot
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    spots = RouteTouristspotSerializer(source='routetouristspot_set',many=True, read_only=True)
    user = UserNameSerializer()
    class Meta:
        model = Route
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = test
        fields = "__all__"

class RouteLikeSerializer(serializers.ModelSerializer):
    user = UserNameSerializer()
    route = RouteSerializer()
    class Meta:
        model = Routelike
        fields = ('user','route')
