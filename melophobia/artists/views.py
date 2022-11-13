from melophobia.models import Artist, ArtistType, Ipi
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from melophobia.artists.serializers import ArtistSerializer, ArtistTypeSerializer, IpiSerializer


class ArtistList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'artist_list.html'

    def get(self, req):
        queryset = Artist.objects.all()

        return Response({'artists': queryset})


class ArtistTypeList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'artist_type_list.html'

    def get(self, req):
        queryset = ArtistType.objects.all()

        return Response({'artist_types': queryset})


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistTypeViewSet(viewsets.ModelViewSet):
    queryset = ArtistType.objects.all()
    serializer_class = ArtistTypeSerializer


class IpiViewSet(viewsets.ModelViewSet):
    queryset = Ipi.objects.all()
    serializer_class = IpiSerializer
