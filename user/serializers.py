from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomAbstractBaseUser
        fields = ('username', 'password', 'email')


class AdminCreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomAbstractBaseUser
        fields = ('username', 'email')


class UserBasicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomAbstractBaseUser
        fields = ('username', 'email')


