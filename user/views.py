from os import stat
from django.shortcuts import render
from django.utils.translation import deactivate_all
from rest_framework import  status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from . import models, serializers


@api_view(['GET'])
def getUserById(request, id):
    try:
        user = models.CustomAbstractBaseUser.object.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialize = serializers.UserBasicInfoSerializer(user)
    return Response(serialize.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getUserByUsername(request, username):
    try:
        user = models.CustomAbstractBaseUser.object.get(username=username)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialize = serializers.UserBasicInfoSerializer(user)
    return Response(serialize.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getUsers(request):
    list = models.CustomAbstractBaseUser.object.all()
    serialize = serializers.UserBasicInfoSerializer(list, many=True)
    return Response(serialize.data, status=status.HTTP_200_OK)
    

@api_view(['POST'])
def createUser(request):
    if request.data['password'] == request.data['confirm_password']:
        serialize = serializers.UserSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize._errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def createUserByAdmin(request):
    serialize = serializers.AdminCreateUserSerializer(data=request.data)
    if serialize.is_valid():
        init_password = get_random_string(length=9)
        serialize.save(password=init_password)
        # send_mail(
        #     'User Registration',
        #     'Please log in using the following creds ' + init_password,
        #     'karlkevinddomingo@gmamil.com',
        #     ['karlkdomingo@gmail.com'],
        #     fail_silently=False,
        # )
        return Response(serialize.data)
    return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def changePassword(request, id):
    try:
        user = models.CustomAbstractBaseUser.object.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialize = serializers.UserSerializer(user, data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)