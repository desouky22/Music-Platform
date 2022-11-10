from rest_framework import serializers
from .models import Album
from artists.serializers import ArtistSerializer


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = ['id', 'artist', 'name', 'release_datetime', 'cost']


class PostAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['artist', 'name', 'release_datetime', 'cost']
