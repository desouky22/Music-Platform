from django.contrib import admin
from .models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ["creation_datetime"]
