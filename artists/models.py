from django.db import models

class Artist(models.Model):
    stage_name = models.CharField(max_length=50, unique=True)
    social_link = models.URLField(blank=True)
    
    
    class Meta:
        ordering = ["stage_name"]
        
    def __str__(self) -> str:
        return f"{self.stage_name}"