from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from melophobia.languages.serializers import LanguageSerializer
from melophobia.models import Language


class LanguageList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'language_list.html'

    def get(self, req):
        queryset = Language.objects.all()

        return Response({'languages': queryset})


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
