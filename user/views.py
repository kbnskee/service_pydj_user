from django.shortcuts import render
from rest_framework import  status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from . import models, serializers


@api_view(['GET'])
def get_user(request):
    return Response()


@api_view(['POST'])
def create_user(request):
    serialize = serializers.UserSerializer(data=request.data)
    return Response()


@api_view(['POST'])
def admin_create_user(request):
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