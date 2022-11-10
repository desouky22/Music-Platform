from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Album
from .serializers import AlbumSerializer, PostAlbumSerializer
from .permissions import IsArtist
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from artists.models import Artist
from artists.serializers import ArtistSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AlbumFilter
from .tasks import sending_emails


class AlbumList(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Album.objects.select_related("artist").all().filter(is_approved=True)
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AlbumFilter

    def post(self, request, *args, **kwargs):
        try:
            artist = Artist.objects.get(user=request.user)
        except Artist.DoesNotExist:
            return Response(
                {"Error": "The user should be an artist"},
                status=status.HTTP_403_FORBIDDEN,
            )
        request.data["artist"] = artist.id
        serializer = PostAlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumListAddingManualFiltering(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AlbumSerializer

    def get_queryset(self):
        queryset = Album.objects.select_related("artist").filter(is_approved=True)
        name = self.request.query_params.get("name__icontains")
        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        cost_lt = name = self.request.query_params.get("cost__lt")
        if cost_lt is not None:
            queryset = queryset.filter(cost__lt=cost_lt)

        cost_gt = name = self.request.query_params.get("cost__gt")
        if cost_gt is not None:
            queryset = queryset.filter(cost__gt=cost_gt)

        return queryset


@api_view(["GET"])
def send_emails(request):
    sending_emails.run(1)
    return Response(status=status.HTTP_200_OK)
