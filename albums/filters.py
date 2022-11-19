from django_filters.rest_framework import FilterSet
from .models import Album


class AlbumFilter(FilterSet):
    class Meta:
        model = Album
        fields = {"name": ["icontains"], "cost": ["lt", "gt"]}
