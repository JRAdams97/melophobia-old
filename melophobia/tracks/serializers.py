from rest_framework import serializers
from melophobia.models import Track, TrackIsrc, TrackIswc, TrackType


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('title', 'track_type', 'artist', 'original_artist', 'favourite', 'wikidata_id')


class TrackIsrcSerializer(serializers.ModelSerializer):
    track = serializers.PrimaryKeyRelatedField(queryset=Track.objects.all())

    class Meta:
        model = TrackIsrc
        fields = ('isrc', 'track')


class TrackIswcSerializer(serializers.ModelSerializer):
    track = serializers.PrimaryKeyRelatedField(queryset=Track.objects.all())

    class Meta:
        model = TrackIswc
        fields = ('iswc', 'track')


class TrackTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackType
        fields = ['name']