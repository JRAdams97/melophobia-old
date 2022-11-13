from melophobia.models import Genre
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from melophobia.genres.serializers import GenreSerializer


class GenreList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'genre_list.html'

    def get(self, req):
        queryset = Genre.objects.all()

        return Response({'genres': queryset})


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
