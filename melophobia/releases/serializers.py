from rest_framework import serializers
from melophobia.models import Artist, Genre, Language, Producer, Release, ReleaseStatus, ReleaseType, Status


class ReleaseSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all(), many=True)
    genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    languages = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), many=True)
    producers = serializers.PrimaryKeyRelatedField(queryset=Producer.objects.all(), many=True)
    types = serializers.PrimaryKeyRelatedField(queryset=ReleaseType.objects.all(), many=True)

    class Meta:
        model = Release
        fields = ('title', 'release_date', 'artists', 'genres', 'types', 'total_tracks', 'missing_tracks',
                  'total_discs', 'missing_discs', 'favourite', 'languages', 'rym_rating', 'aoty_rank', 'bea_rank',
                  'christgau_rating', 'hull_rating', 'scaruffi_rating', 'metacritic', 'pitchfork_rating',
                  'art_quality', 'tag_quality', 'bitrate', 'producers', 'wikidata_id', 'release_status',
                  'log_status', 'description')


class ReleaseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseStatus
        fields = ['name']


class ReleaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseType
        fields = ['name']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('name', 'colour')
