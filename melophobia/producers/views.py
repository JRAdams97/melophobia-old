from rest_framework import viewsets
from melophobia.producers.serializers import ProducerSerializer
from melophobia.models import Producer


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
