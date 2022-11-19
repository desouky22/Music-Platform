from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.authentication import TokenAuthentication
from .models import User
from authentication.serializers import UserSerializer
from .permissions import IsTheCurrentUser
from knox.auth import TokenAuthentication as knox_token


class UserAPIView(APIView):
    authentication_classes = [knox_token]
    permission_classes = [IsTheCurrentUser]

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=kwargs["pk"])
            serializer = UserSerializer(user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=kwargs["pk"])
            serializer = UserSerializer(instance=user, data=request.data)
            self.check_object_permissions(self.request, user)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=kwargs["pk"])
            serializer = UserSerializer(instance=user, data=request.data, partial=True)
            self.check_object_permissions(self.request, user)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
