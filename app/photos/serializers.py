from rest_framework import serializers
from app.photos.models import Album, Photo

class PhotoSerializer(serializers.ModelSerializer):
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())  # Handle UUID lookup

    class Meta:
        model = Photo
        fields = ['id', 'album', 'title', 'image', 'image_url']

class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.UUIDField(read_only=True, source='user.id')
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'user', 'title', 'photos']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    