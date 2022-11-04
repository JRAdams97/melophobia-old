from melophobia.models import Country
from rest_framework import viewsets
from melophobia.countries.serializers import CountrySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
