from melophobia.models import Genre
from rest_framework import viewsets
from melophobia.genres.serializers import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
