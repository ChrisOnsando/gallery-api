from django.urls import path
from app.photos.views import (
    AlbumListCreateView, 
    AlbumRetrieveUpdateDeleteView,
    PhotoListCreateView, 
    PhotoRetrieveUpdateDeleteView,
)

urlpatterns = [
    path('albums/', AlbumListCreateView.as_view(), name='album-list-create'),
    path('albums/<uuid:id>/', AlbumRetrieveUpdateDeleteView.as_view(), name='album-detail'),
    path('photos/', PhotoListCreateView.as_view(), name='photo-list-create'),
    path('photos/<uuid:id>/', PhotoRetrieveUpdateDeleteView.as_view(), name='photo-detail'),
]
