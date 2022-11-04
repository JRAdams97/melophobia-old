from rest_framework import viewsets
from melophobia.statuses.serializers import StatusSerializer
from melophobia.models import Status


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
