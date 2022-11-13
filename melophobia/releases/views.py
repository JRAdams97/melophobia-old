from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from melophobia.releases.serializers import ReleaseSerializer, ReleaseTypeSerializer, ReleaseStatusSerializer,\
                                            StatusSerializer
from melophobia.models import Release, ReleaseStatus, ReleaseType, Status


class ReleaseList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'release_list.html'

    def get(self, req):
        queryset = Release.objects.all()

        return Response({'releases': queryset})


class ReleaseStatusList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'release_status_list.html'

    def get(self, req):
        queryset = ReleaseStatus.objects.all()

        return Response({'release_statuses': queryset})


class ReleaseTypeList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'release_type_list.html'

    def get(self, req):
        queryset = ReleaseType.objects.all()

        return Response({'release_types': queryset})


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class ReleaseTypeViewSet(viewsets.ModelViewSet):
    queryset = ReleaseType.objects.all()
    serializer_class = ReleaseTypeSerializer


class ReleaseStatusViewSet(viewsets.ModelViewSet):
    queryset = ReleaseStatus.objects.all()
    serializer_class = ReleaseStatusSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
