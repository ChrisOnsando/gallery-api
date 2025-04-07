from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Album, Photo
from .serializers import AlbumSerializer, PhotoSerializer
from app.photos.permissions import IsUser

class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class AlbumRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated, IsUser]
    lookup_field = 'id'

class PhotoListCreateView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(album__user=self.request.user)

class PhotoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated, IsUser]
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter(album__user=self.request.user)
    