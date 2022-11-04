from rest_framework import viewsets
from melophobia.media.serializers import MediaSerializer
from melophobia.models import Media


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
