from rest_framework import viewsets
from melophobia.languages.serializers import LanguageSerializer
from melophobia.models import Language


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
