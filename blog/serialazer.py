from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,Serializer

from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',"role")

class SimpleUserSerializer(Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

