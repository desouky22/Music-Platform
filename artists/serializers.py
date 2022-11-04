from .models import Artist
from rest_framework import serializers
from albums.serializers import AlbumSerializer


class ArtistSerializer(serializers.ModelSerializer):
    # approved_albums = serializers.SerializerMethodField(
    #     method_name="calculate_approved_albums"
    # )

    # albums = AlbumSerializer(many=True)

    # def calculate_approved_albums(self, obj):
    #     return obj.albums.filter(is_approved=True).count()

    class Meta:
        model = Artist
        fields = ["id", "stage_name", "social_link"]
