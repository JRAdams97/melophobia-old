from rest_framework import serializers
from melophobia.models import Ipi, Producer


class ProducerSerializer(serializers.ModelSerializer):
    ipis = serializers.PrimaryKeyRelatedField(queryset=Ipi.objects.all(), many=True)

    class Meta:
        model = Producer
        fields = ('name', 'birth_date', 'birth_area', 'birth_country_id', 'death_date', 'death_area',
                  'death_country_id', 'favourite', 'ipis', 'isni', 'wikidata_id')
