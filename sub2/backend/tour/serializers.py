from django.db.models import fields
from rest_framework import serializers

from .models import Touristspot

class tourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Touristspot
        fields ="__all__"