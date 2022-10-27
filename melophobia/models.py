# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ArtistType(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        app_label = 'artists'
        managed = False
        db_table = 'artist_type'


class Country(models.Model):
    name = models.TextField(unique=True)
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'countries'
        managed = False
        db_table = 'country'


class Artist(models.Model):
    name = models.TextField()
    formation_date = models.CharField(max_length=10, blank=True, null=True)
    formation_area = models.TextField(blank=True, null=True)
    formation_country = models.ForeignKey(Country, models.DO_NOTHING, related_name='formationCountry')
    disband_date = models.CharField(max_length=10, blank=True, null=True)
    disband_area = models.TextField(blank=True, null=True)
    disband_country = models.ForeignKey(
        Country, models.DO_NOTHING, blank=True, null=True, related_name='disbandCountry')
    favourite = models.BooleanField()
    artist_type = models.ForeignKey(ArtistType, models.DO_NOTHING)
    isni = models.CharField(unique=True, max_length=19, blank=True, null=True)
    amazon_music_id = models.TextField(unique=True, blank=True, null=True)
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'artists'
        managed = False
        db_table = 'artist'


class Genre(models.Model):
    name = models.TextField(unique=True)
    origin_year = models.SmallIntegerField()
    favourite = models.BooleanField()
    parent_genre = models.ForeignKey('self', models.DO_NOTHING, db_column='parent_genre', blank=True, null=True)
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'genres'
        managed = False
        db_table = 'genre'


class ArtistGenres(models.Model):
    artist = models.OneToOneField(Artist, models.DO_NOTHING, primary_key=True)
    genre = models.ForeignKey(Genre, models.DO_NOTHING)

    class Meta:
        app_label = 'artists'
        managed = False
        db_table = 'artist_genres'
        unique_together = (('artist', 'genre'),)


class Ipi(models.Model):
    ipi_id = models.TextField(primary_key=True)

    class Meta:
        app_label = 'artists'
        managed = False
        db_table = 'ipi'


class ArtistIpis(models.Model):
    artist = models.OneToOneField(Artist, models.DO_NOTHING, primary_key=True)
    ipi = models.OneToOneField(Ipi, models.DO_NOTHING)

    class Meta:
        app_label = 'artists'
        managed = False
        db_table = 'artist_ipis'
        unique_together = (('artist', 'ipi'),)


class Label(models.Model):
    name = models.TextField()
    formation_date = models.CharField(max_length=10, blank=True, null=True)
    formation_area = models.TextField(blank=True, null=True)
    formation_country = models.ForeignKey(Country, models.DO_NOTHING)
    closing_date = models.CharField(max_length=10, blank=True, null=True)
    favourite = models.BooleanField()
    label_code = models.TextField(unique=True, blank=True, null=True)
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'labels'
        managed = False
        db_table = 'label'


class ReleaseStatus(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release_status'


class Status(models.Model):
    name = models.TextField(unique=True)
    colour = models.CharField(unique=True, max_length=7)

    class Meta:
        app_label = 'statuses'
        managed = False
        db_table = 'status'


class Release(models.Model):
    title = models.TextField()
    release_date = models.CharField(max_length=10)
    total_tracks = models.SmallIntegerField()
    missing_tracks = models.SmallIntegerField()
    total_discs = models.SmallIntegerField()
    missing_discs = models.SmallIntegerField()
    favourite = models.BooleanField()
    rym_rating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    aoty_rank = models.SmallIntegerField(blank=True, null=True)
    bea_rank = models.SmallIntegerField(blank=True, null=True)
    christgau_rating = models.TextField(blank=True, null=True)
    hull_rating = models.TextField(blank=True, null=True)
    scaruffi_rating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    metacritic = models.SmallIntegerField(blank=True, null=True)
    pitchfork_rating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    art_quality = models.SmallIntegerField()
    tag_quality = models.SmallIntegerField()
    bitrate = models.TextField()
    asin = models.CharField(unique=True, max_length=10, blank=True, null=True)
    wikidata_id = models.TextField(unique=True, blank=True, null=True)
    release_status = models.ForeignKey(ReleaseStatus, models.DO_NOTHING)
    log_status = models.ForeignKey(Status, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release'


class CatalogueItems(models.Model):
    label = models.ForeignKey(Label, models.DO_NOTHING)
    release = models.ForeignKey(Release, models.DO_NOTHING, blank=True, null=True)
    catalogue_id = models.TextField()
    release_status = models.ForeignKey(ReleaseStatus, models.DO_NOTHING)

    class Meta:
        app_label = 'labels'
        managed = False
        db_table = 'catalogue_items'


class Media(models.Model):
    name = models.TextField(unique=True)
    type = models.TextField()
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'media'
        managed = False
        db_table = 'media'


class CatalogueMedia(models.Model):
    global_catalogue = models.OneToOneField(CatalogueItems, models.DO_NOTHING, primary_key=True)
    media = models.ForeignKey(Media, models.DO_NOTHING)

    class Meta:
        app_label = 'labels'
        managed = False
        db_table = 'catalogue_media'
        unique_together = (('global_catalogue', 'media'),)


class LabelIpis(models.Model):
    label = models.OneToOneField(Label, models.DO_NOTHING, primary_key=True)
    ipi = models.OneToOneField(Ipi, models.DO_NOTHING)

    class Meta:
        app_label = 'labels'
        managed = False
        db_table = 'label_ipis'
        unique_together = (('label', 'ipi'),)


class Language(models.Model):
    name = models.TextField(unique=True)
    charset = models.TextField()
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'languages'
        managed = False
        db_table = 'language'


class Producer(models.Model):
    name = models.TextField()
    birth_date = models.CharField(max_length=10, blank=True, null=True)
    birth_area = models.TextField(blank=True, null=True)
    birth_country = models.ForeignKey(Country, models.DO_NOTHING, related_name='birthCountry')
    death_date = models.CharField(max_length=10, blank=True, null=True)
    death_area = models.TextField(blank=True, null=True)
    death_country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True, related_name='deathCountry')
    favourite = models.BooleanField()
    isni = models.CharField(unique=True, max_length=19, blank=True, null=True)
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'producers'
        managed = False
        db_table = 'producer'


class ProducerIpis(models.Model):
    producer = models.OneToOneField(Producer, models.DO_NOTHING, primary_key=True)
    ipi = models.OneToOneField(Ipi, models.DO_NOTHING)

    class Meta:
        app_label = 'producers'
        managed = False
        db_table = 'producer_ipis'
        unique_together = (('producer', 'ipi'),)


class ReleaseArtists(models.Model):
    release = models.OneToOneField(Release, models.DO_NOTHING, primary_key=True)
    artist = models.ForeignKey(Artist, models.DO_NOTHING)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release_artists'
        unique_together = (('release', 'artist'),)


class ReleaseGenres(models.Model):
    release = models.OneToOneField(Release, models.DO_NOTHING, primary_key=True)
    genre = models.ForeignKey(Genre, models.DO_NOTHING)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release_genres'
        unique_together = (('release', 'genre'),)


class ReleaseLanguages(models.Model):
    release = models.OneToOneField(Release, models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey(Language, models.DO_NOTHING)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release_languages'
        unique_together = (('release', 'language'),)


class ReleaseProducers(models.Model):
    release = models.OneToOneField(Release, models.DO_NOTHING, primary_key=True)
    producer = models.ForeignKey(Producer, models.DO_NOTHING)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release_producers'
        unique_together = (('release', 'producer'),)


class ReleaseType(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release_type'


class ReleaseTypes(models.Model):
    release = models.OneToOneField(Release, models.DO_NOTHING, primary_key=True)
    release_type = models.ForeignKey(ReleaseType, models.DO_NOTHING)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release_types'
        unique_together = (('release', 'release_type'),)


class TrackType(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        app_label = 'tracks'
        managed = False
        db_table = 'track_type'


class Track(models.Model):
    title = models.TextField()
    track_type = models.ForeignKey(TrackType, models.DO_NOTHING)
    artist = models.ForeignKey(Artist, models.DO_NOTHING, related_name='artist')
    original_artist = models.ForeignKey(
        Artist, models.DO_NOTHING, blank=True, null=True, related_name='originalArtist')
    favourite = models.BooleanField()
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'tracks'
        managed = False
        db_table = 'track'


class TrackIsrc(models.Model):
    track = models.OneToOneField(Track, models.DO_NOTHING, primary_key=True)
    isrc = models.CharField(unique=True, max_length=15)

    class Meta:
        app_label = 'tracks'
        managed = False
        db_table = 'track_isrc'
        unique_together = (('track', 'isrc'),)


class TrackIswc(models.Model):
    track = models.OneToOneField(Track, models.DO_NOTHING, primary_key=True)
    iswc = models.CharField(unique=True, max_length=15)

    class Meta:
        app_label = 'tracks'
        managed = False
        db_table = 'track_iswc'
        unique_together = (('track', 'iswc'),)
