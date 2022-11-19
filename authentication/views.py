from django.contrib.auth import login as auth_login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .serializers import RegisterSerializer, UserSerializer
from users.models import User

from knox.auth import AuthToken
from knox.views import LoginView


class Register(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(LoginView):
    permission_classes = [AllowAny]

    def post(self, request, format=None, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            deserialized_user = UserSerializer(user)
            auth_login(request, user)
            instance, token = AuthToken.objects.create(user)
            return Response({"Knox Token": token, "User": deserialized_user.data})
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
