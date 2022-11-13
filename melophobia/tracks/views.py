from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from melophobia.tracks.serializers import TrackSerializer, TrackIsrcSerializer, TrackIswcSerializer, TrackTypeSerializer
from melophobia.models import Track, TrackIsrc, TrackIswc, TrackType


class TrackList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'track_list.html'

    def get(self, req):
        queryset = Track.objects.all()

        return Response({'tracks': queryset})


class TrackIsrcList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'track_isrc_list.html'

    def get(self, req):
        queryset = TrackIsrc.objects.all()

        return Response({'track_isrc_list': queryset})


class TrackIswcList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'track_iswc_list.html'

    def get(self, req):
        queryset = TrackIswc.objects.all()

        return Response({'track_iswc_list': queryset})


class TrackTypeList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'track_type_list.html'

    def get(self, req):
        queryset = TrackType.objects.all()

        return Response({'track_types': queryset})


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackIsrcViewSet(viewsets.ModelViewSet):
    queryset = TrackIsrc.objects.all()
    serializer_class = TrackIsrcSerializer


class TrackIswcViewSet(viewsets.ModelViewSet):
    queryset = TrackIswc.objects.all()
    serializer_class = TrackIswcSerializer


class TrackTypeViewSet(viewsets.ModelViewSet):
    queryset = TrackType.objects.all()
    serializer_class = TrackTypeSerializer
