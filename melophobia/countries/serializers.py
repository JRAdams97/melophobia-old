from rest_framework import serializers
from melophobia.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'country_code', 'wikidata_id')
