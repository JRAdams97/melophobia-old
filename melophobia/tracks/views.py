from rest_framework import viewsets
from melophobia.tracks.serializers import TrackSerializer, TrackIsrcSerializer, TrackIswcSerializer, TrackTypeSerializer
from melophobia.models import Track, TrackIsrc, TrackIswc, TrackType


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
