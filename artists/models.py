from django.db import models
from users.models import User


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    stage_name = models.CharField(
        max_length=50,
        unique=True,
    )
    social_link = models.URLField(blank=True, default="", null=False)

    class Meta:
        ordering = ["stage_name"]

    def __str__(self) -> str:
        return f"{self.stage_name}"
