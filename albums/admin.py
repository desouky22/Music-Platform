from django.contrib import admin
from .models import Album, Song


class InlineSong(admin.StackedInline):
    model = Song
    extra = 0
    min_num = 1


class AlbumDataAdmin(admin.ModelAdmin):
    inlines = [InlineSong]


admin.site.register(Album, AlbumDataAdmin)
admin.site.register(Song)
