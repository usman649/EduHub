from django.contrib.auth import authenticate

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serialazer import UserSerializer, SimpleUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import ModelViewSet


@swagger_auto_schema(
    method="post",
    responses={200: UserSerializer(many=True)},
    tags=["User"],
    request_body=UserSerializer,
)
@api_view(http_method_names=['POST'])
def register_view(request):
    serial = UserSerializer(data=request.data)
    serial.is_valid(raise_exception=True)
    password = serial.validated_data['password']
    user_obj = serial.save(password=make_password(password))
    return Response(data={"message": f"User {user_obj.username} created successfully."}, status=status.HTTP_201_CREATED)


@swagger_auto_schema(
    method="post",
    tags=["User"],
    request_body=SimpleUserSerializer,

)
@api_view(http_method_names=['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user_mod = User.objects.filter(username=username).first()
    if not user_mod:
        return Response({'error': 'Username does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    if not check_password(password, user_mod.password):
        return Response({'error': 'password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

    refresh_token = RefreshToken.for_user(user_mod)
    access_token = refresh_token.access_token

    return Response(data={"access_token": str(access_token), "refresh_token": str(refresh_token)},
                    status=status.HTTP_200_OK)


@swagger_auto_schema(
    method="get",
    tags=["User"],
)
@api_view(http_method_names=['GET'])
def me_view(request):
    return Response(data={"username": request.user.username}, status=status.HTTP_200_OK)
