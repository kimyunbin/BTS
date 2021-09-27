from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import City

User = get_user_model()

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