from django.db import models
from artists.models import Artist
from django_extensions.db.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from pilkit.processors import Thumbnail
from django.core.validators import FileExtensionValidator


class Album(TimeStampedModel):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name="albums", null=False, blank=False
    )
    name = models.CharField(max_length=100, default="New Album")
    release_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    is_approved = models.BooleanField(
        default=False, help_text="Approve the album if its name is not explicit"
    )


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100, default=album.name)
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    Thumbnail = ImageSpecField(
        source="image",
        processors=[Thumbnail(200, 100)],
        format="JPEG",
        options={"quality": 60},
    )
    audio = models.FileField(
        upload_to="audio/",
        validators=[FileExtensionValidator(allowed_extensions=["mp3", "wav"])],
        null=False,
        blank=False,
    )
