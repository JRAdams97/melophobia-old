from rest_framework import serializers
from melophobia.models import Artist, ArtistType


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'formation_date', 'formation_area', 'formation_country', 'disband_date',
                  'disband_area', 'disband_country', 'favourite', 'artist_type', 'isni', 'amazon_music_id',
                  'wikidata_id']


class ArtistTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistType
        fields = ['name']
