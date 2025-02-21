from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from app.AboutAcademy.models import *
from app.AboutAcademy.serializers import *
from django.http import FileResponse
from rest_framework.decorators import action
# Create your views here.

class AboutUsAPI(GenericViewSet,
                 mixins.ListModelMixin):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class DevStrategyAPI(GenericViewSet,
                     mixins.ListModelMixin):
    queryset = DevStrategy.objects.all()
    serializer_class = DevStrategySerializers

class DevStrategyPhotoAPI(GenericViewSet,
                          mixins.ListModelMixin):
    queryset = DevStrategyPhoto.objects.all()
    serializer_class = DevStrategyPhotoSerializer

class MissionAPI(GenericViewSet,
                 mixins.ListModelMixin):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializers

class DocumentAPI(GenericViewSet,
                  mixins.ListModelMixin, 
                  mixins.RetrieveModelMixin,):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        document = self.get_object()
        return FileResponse(document.file.open(), as_attachment=True)
    
class AchievementsAPI(GenericViewSet,
                      mixins.ListModelMixin):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer

class HistoryAPI(GenericViewSet,
                 mixins.ListModelMixin):
    queryset = History.objects.all()
    serializer_class = HistorySerializer