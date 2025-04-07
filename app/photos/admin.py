from django.contrib import admin

from app.photos.models import Photo, Album

admin.site.register(Photo)
admin.site.register(Album)
