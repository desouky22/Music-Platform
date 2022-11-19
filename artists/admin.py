from django.contrib import admin
from .models import Artist
from albums.models import Album

# removed in Task 4
# class AlbumInline(admin.TabularInline):
#     model = Album


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["stage_name", "social_link", "approved_albums"]
    
    # removed in Task 4
    # inlines = [AlbumInline]

    def approved_albums(self, artist):
        return artist.albums.filter(is_approved=True).count()
