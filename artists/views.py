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


class ArtistDetail(APIView):
    def get(self, request, *args, **kwargs):
        try:
            artist = Artist.objects.get(pk=kwargs["pk"])
            serializer = ArtistSerializer(artist)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            artist = Artist.objects.get(pk=kwargs["pk"])
            serializer = ArtistSerializer(instance=artist, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            artist = Artist.objects.get(pk=kwargs["pk"])
            artist.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Artist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
