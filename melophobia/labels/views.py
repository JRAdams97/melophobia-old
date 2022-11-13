from melophobia.models import CatalogueItems, Label
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from melophobia.labels.serializers import CatalogueItemsSerializer, LabelSerializer


class LabelList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'label_list.html'

    def get(self, req):
        queryset = Label.objects.all()

        return Response({'labels': queryset})


class CatalogueItemsViewSet(viewsets.ModelViewSet):
    serializer_class = CatalogueItemsSerializer

    def get_queryset(self):
        return CatalogueItems.objects.filter(label=self.kwargs['label_pk'])


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
