from rest_framework import serializers
from .models import FireIncident, IncidentPhoto
from django.conf import settings

class IncidentPhotoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = IncidentPhoto
        fields = ('id','image','image_url','caption')

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None

class FireIncidentSerializer(serializers.ModelSerializer):
    photos = IncidentPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = FireIncident
        fields = '__all__'
