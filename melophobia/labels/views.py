from melophobia.models import CatalogueItems, Label
from rest_framework import viewsets
from melophobia.labels.serializers import CatalogueItemsSerializer, LabelSerializer


class CatalogueItemsViewSet(viewsets.ModelViewSet):
    serializer_class = CatalogueItemsSerializer

    def get_queryset(self):
        return CatalogueItems.objects.filter(label=self.kwargs['label_pk'])


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
