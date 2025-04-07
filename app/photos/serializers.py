from rest_framework import serializers
from app.photos.models import Album, Photo
from app.user.serializers import ProfileSerializer

class PhotoSerializer(serializers.ModelSerializer):
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())  # Handle UUID lookup

    class Meta:
        model = Photo
        fields = ['id', 'album', 'title', 'image', 'image_url']

class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.UUIDField(read_only=True, source='user.id')
    photos = PhotoSerializer(many=True, read_only=True)
    profile = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ['id', 'user', 'title', 'photos', 'profile']

    def get_profile(self, obj):
        profile = obj.user.profile
        return ProfileSerializer(profile, context=self.context).data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    