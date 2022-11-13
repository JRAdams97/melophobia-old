from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from melophobia.media.serializers import MediaSerializer
from melophobia.models import Media


class MediaList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'media_list.html'

    def get(self, req):
        queryset = Media.objects.all()

        return Response({'media_list': queryset})


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
