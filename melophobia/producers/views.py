from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from melophobia.producers.serializers import ProducerSerializer
from melophobia.models import Producer


class ProducerList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'producer_list.html'

    def get(self, req):
        queryset = Producer.objects.all()

        return Response({'producers': queryset})


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
