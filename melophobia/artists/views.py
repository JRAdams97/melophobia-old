from melophobia.models import Artist, ArtistType, Ipi
from rest_framework import viewsets
from melophobia.artists.serializers import ArtistSerializer, ArtistTypeSerializer, IpiSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistTypeViewSet(viewsets.ModelViewSet):
    queryset = ArtistType.objects.all()
    serializer_class = ArtistTypeSerializer


class IpiViewSet(viewsets.ModelViewSet):
    queryset = Ipi.objects.all()
    serializer_class = IpiSerializer
