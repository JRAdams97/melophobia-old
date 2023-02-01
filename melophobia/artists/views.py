from django.shortcuts import get_object_or_404, redirect
from melophobia.models import Artist, ArtistType, Ipi
from rest_framework import status, viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from melophobia.artists.serializers import ArtistSerializer, ArtistTypeSerializer, IpiSerializer


class ArtistList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'artist_list.html'

    def get(self, req):
        artists = Artist.objects.all()

        return Response({'artists': artists})


class ArtistDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'artist_detail.html'

    def get(self, req, pk):
        artist = Artist.objects.get(id=pk)

        return Response({'artist': artist})


class ArtistCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'artist_create.html'

    def get(self, req):
        serializer = ArtistSerializer()

        return Response({'serializer': serializer})

    def post(self, req):
        serializer = ArtistSerializer(data=req.data)

        if serializer.is_valid():
            serializer.save()

            return redirect('artists')

        else:
            return Response({'serializer': serializer})


class ArtistUpdate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'artist_update.html'

    def get(self, req, pk):
        artist = Artist.objects.get(id=pk)
        serializer = ArtistSerializer(instance=artist)

        return Response({'serializer': serializer, 'pk': pk})

    def post(self, req, pk):
        artist = Artist.objects.get(id=pk)
        serializer = ArtistSerializer(artist, data=req.data)

        if serializer.is_valid():
            serializer.save()

            return redirect('../../artists')

        else:
            return Response({'serializer': serializer, 'artist': artist, 'pk': pk})


class ArtistDelete(APIView):
    def get(self, req, pk):
        artist = Artist.objects.get(id=pk)
        artist.delete()

        return redirect('../../artists')


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
