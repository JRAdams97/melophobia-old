from melophobia.models import Country
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from melophobia.countries.serializers import CountrySerializer


class CountryList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'country_list.html'

    def get(self, req):
        queryset = Country.objects.all()

        return Response({'countries': queryset})


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
