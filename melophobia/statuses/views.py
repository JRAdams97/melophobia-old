from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from melophobia.statuses.serializers import StatusSerializer
from melophobia.models import Status


class StatusList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'status_list.html'

    def get(self, req):
        queryset = Status.objects.all()

        return Response({'statuses': queryset})


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
