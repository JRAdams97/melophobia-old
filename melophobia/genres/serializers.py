from rest_framework import serializers
from melophobia.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    parent_genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)

    class Meta:
        model = Genre
        fields = ('name', 'origin_year', 'favourite', 'parent_genres', 'wikidata_id')