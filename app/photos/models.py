from django.db import models
import uuid
from app.user.models import User 
from app.abstracts import TimeStampedModel


class Album(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Photo(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/', null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True)  

    def __str__(self):
        return self.title
    
