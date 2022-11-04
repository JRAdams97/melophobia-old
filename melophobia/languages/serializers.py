from rest_framework import serializers
from melophobia.models import Language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name', 'charset', 'wikidata_id')