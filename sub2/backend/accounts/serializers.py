
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import City, WishList
from tour.serializers import UserNameSerializer,tourSerializer
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
User = get_user_model()
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserCreateSerializer(serializers.Serializer):
    username = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    nickname =  serializers.CharField()
    budget = serializers.IntegerField()
    travelers = serializers.IntegerField()
    companion = serializers.BooleanField()
    transportation = serializers.CharField()
    selection = serializers.CharField()
    age = serializers.IntegerField()
    activity =  serializers.CharField()
    sex = serializers.BooleanField()

    def create(self, validated_data):
        user = User.objects.create( # User 생성
            username=validated_data['username'],
            nickname=validated_data['nickname'],
            budget=validated_data['budget'],
            travelers=validated_data['travelers'],
            companion=validated_data['companion'],
            transportation=validated_data['transportation'],
            selection=validated_data['selection'],
            age=validated_data['age'],
            activity=validated_data['activity'],
            sex=validated_data['sex'],
        )
        user.set_password(validated_data['password'])

        user.save()
        return user



class UserLoginSerializer(serializers.Serializer):
    username = serializers.EmailField(max_length=255,)
    nickname = serializers.CharField(max_length=128, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(username=username, password=password)

        if user is None:
            return {
                'username': 'None'
            }
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload) # 토큰 발행
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'nickname': user.nickname,
            'token': jwt_token,
            'username':user.username
        }

class UserSerializer(serializers.ModelSerializer):
    # write_only는 시리얼라이징은 하지만 응답에는 포함시키지 않는다는 의미
    # 비밀번호를 응답에 표현한다면 보안상의 유출이 되는 것이기 떄문

    password = serializers.CharField(write_only=True)

    class Meta : 
        model = User
        # fields = '__all__'
        exclude = ('profile','authenticated')
        # fields = ('username', 'password','nickname')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('state','city','code','satis')

class WishSerialzer(serializers.ModelSerializer):
    user = UserNameSerializer()
    Touristspot = tourSerializer()
    class Meta:
        model = WishList
        fields = ('user','Touristspot')