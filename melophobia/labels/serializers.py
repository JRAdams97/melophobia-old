from rest_framework import serializers
from melophobia.models import CatalogueItems, Media, Ipi, Label


class CatalogueItemsSerializer(serializers.ModelSerializer):
    media = serializers.PrimaryKeyRelatedField(queryset=Media.objects.all(), many=True)

    class Meta:
        model = CatalogueItems
        fields = ('label', 'release', 'catalogue_id', 'media', 'release_status')


class LabelSerializer(serializers.ModelSerializer):
    ipis = serializers.PrimaryKeyRelatedField(queryset=Ipi.objects.all(), many=True)

    class Meta:
        model = Label
        fields = ('name', 'formation_date', 'formation_area', 'formation_country', 'closing_date', 'favourite',
                  'label_code', 'ipis', 'wikidata_id')
