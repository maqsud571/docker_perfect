from rest_framework import serializers
from .models import UserModel

class UserSRL(serializers.ModelSerializer):
    class Meta: 
        model = UserModel
        fields = "__all__"

class Login(serializers.ModelSerializer):
    class Meta: 
        model = UserModel
        fields = "__all__"