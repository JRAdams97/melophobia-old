from rest_framework import serializers
from melophobia.models import Artist, ArtistType, Genre, Ipi


class ArtistSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    ipis = serializers.PrimaryKeyRelatedField(queryset=Ipi.objects.all(), many=True)

    class Meta:
        model = Artist
        fields = ('name', 'formation_date', 'formation_area', 'formation_country', 'disband_date', 'disband_area',
                  'disband_country', 'genres', 'favourite', 'artist_type', 'isni', 'amazon_music_id', 'ipis',
                  'wikidata_id')


class ArtistTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistType
        fields = ['name']


class IpiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ipi
        fields = ['ipi_id']