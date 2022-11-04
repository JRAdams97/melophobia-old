from rest_framework import viewsets
from melophobia.releases.serializers import ReleaseSerializer, ReleaseTypeSerializer, ReleaseStatusSerializer,\
                                            StatusSerializer
from melophobia.models import Release, ReleaseStatus, ReleaseType, Status


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
