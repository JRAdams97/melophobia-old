from melophobia.models import Artist, ArtistType
from rest_framework import viewsets
from melophobia.artists.serializers import ArtistSerializer, ArtistTypeSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistTypeViewSet(viewsets.ModelViewSet):
    queryset = ArtistType.objects.all()
    serializer_class = ArtistTypeSerializer
