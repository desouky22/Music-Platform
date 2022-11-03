from django.db import models
from artists.models import Artist


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=100, default="New Album")
    creation_datetime = models.DateTimeField(auto_now_add=True, editable=False)
    release_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    is_approved = models.BooleanField(
        default=False, help_text="Approve the album if its name is not explicit"
    )
