from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from .models import Artist
from .serializers import ArtistSerializer


# changed to class based view
# @api_view(["GET"])
# def get_all_artists(request, *args, **kwargs):
#     queryset = Artist.objects.prefetch_related('albums').all()
#     serializer = ArtistSerializer(queryset, many=True)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)


class ArtistList(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        queryset = Artist.objects.prefetch_related("albums").all()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
