from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Artist
from .serializers import ArtistSerializer


# changed to class based view
# @api_view(["GET"])
# def get_all_artists(request, *args, **kwargs):
#     queryset = Artist.objects.prefetch_related('albums').all()
#     serializer = ArtistSerializer(queryset, many=True)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)


class ArtistList(APIView):
    def get(self, *args, **kwargs):
        queryset = Artist.objects.prefetch_related("albums").all()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    