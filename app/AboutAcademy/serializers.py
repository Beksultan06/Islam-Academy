from rest_framework import serializers
from app.AboutAcademy.models import *
from django.conf import settings

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'title', 'description', 'title_phone_number', 'phone_number', 'title_adress', 'adress', 'title_operating_mode', 'operating_mode', 'link_map']
    
class DevStrategySerializers(serializers.ModelSerializer):
    class Meta:
        model = DevStrategy
        fields = ['id', 'title', 'description']

class DevStrategyPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevStrategyPhoto
        fields = ['id', 'photo']

class MissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ['id', 'title', 'description']

class DocumentSerializer(serializers.ModelSerializer):
    open_url = serializers.SerializerMethodField()
    download_url = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'open_url', 'download_url']
        extra_kwargs = {'file': {'read_only': True}}

    def get_open_url(self, obj):
        return f'http://127.0.0.1:8000{obj.file.url}/'
    
    def get_download_url(self, obj):

        return f'http://127.0.0.1:8000/ru/api/v1/AboutAcademy/Document/{obj.id}/download/'
    
class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = ['id', 'title', 'description']

class HistorySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = History
        fields = ['id', 'title', 'description', 'images']

    def get_images(self, obj):
        request = self.context.get('request')
        images = obj.historyobject_set.all()

        image_urls = []
        for image in images:
            if image.image:
                image_url = image.image.url
                if request:
                    image_url = request.build_absolute_uri(image_url)
                else:
                    image_url = f"{settings.MEDIA_URL}{image.image}"
                image_urls.append(image_url)

        return image_urls
