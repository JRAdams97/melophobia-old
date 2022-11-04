from rest_framework import serializers
from melophobia.models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('name', 'type', 'wikidata_id')
