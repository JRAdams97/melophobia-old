# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.core.validators import RegexValidator
from django.db import models

# Validation regexes
DATE_REGEX = '^(?:0\\d|1\\d|2\\d|3[0-1])\\/(?:0\\d|1[0-2])\\/\\d{4}$'
ISNI_REGEX = '^(?:\\d{4} ){3}\\d{4}$'

# Validation messages
DATE_V_MSG = "Dates must be in 'dd/MM/yyyy' format."
ISNI_V_MSG = "ISNIs must be in the format 'xxxx xxxx xxxx xxxx'."


class ArtistType(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        app_label = 'artists'
        managed = False
        db_table = 'artist_type'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.TextField(unique=True)
    country_code = models.TextField(max_length=2, unique=True, blank=True, null=True)
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'countries'
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.TextField(unique=True)
    origin_year = models.SmallIntegerField()
    favourite = models.BooleanField()
    parent_genres = models.ManyToManyField('Genre', related_name="genre_hierarchy", through='GenreHierarchy',
                                           through_fields=('genre', 'parent_genre'))
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'genres'
        managed = False
        db_table = 'genre'

    def __str__(self):
        return self.name


class GenreHierarchy(models.Model):
    genre = models.OneToOneField(Genre, models.CASCADE, primary_key=True, related_name="mainGenre")
    parent_genre = models.ForeignKey(Genre, models.CASCADE, related_name="parentGenre")

    class Meta:
        app_label = 'genres'
        managed = False
        db_table = 'genrea_hierarchy'
        unique_together = (('genre', 'parent_genre'),)


class Ipi(models.Model):
    ipi_id = models.TextField(primary_key=True)

    class Meta:
        verbose_name = 'IPI'
        verbose_name_plural = 'IPIs'
        app_label = 'artists'
        managed = False
        db_table = 'ipi'


class Artist(models.Model):
    name = models.TextField()
    formation_date = models.CharField(max_length=10, blank=True, null=True, verbose_name='Formation Date',
                                      validators=[RegexValidator(regex=DATE_REGEX, message=DATE_V_MSG)])
    formation_area = models.TextField(blank=True, null=True, verbose_name='Formation Area')
    formation_country = models.ForeignKey(Country, models.CASCADE, related_name='formationCountry',
                                          verbose_name='Formation Country')
    disband_date = models.CharField(max_length=10, blank=True, null=True, verbose_name='Disband Date',
                                    validators=[RegexValidator(regex=DATE_REGEX, message=DATE_V_MSG)])
    disband_area = models.TextField(blank=True, null=True, verbose_name='Disband Area')
    disband_country = models.ForeignKey(
        Country, models.CASCADE, blank=True, null=True, related_name='disbandCountry',
        verbose_name='Disband Country')
    genres = models.ManyToManyField(Genre, related_name="artist", through='ArtistGenres',
                                    through_fields=('artist', 'genre'))
    favourite = models.BooleanField()
    artist_type = models.ForeignKey(ArtistType, models.CASCADE, verbose_name='Artist Type')
    isni = models.CharField(unique=True, max_length=19, blank=True, null=True, verbose_name='ISNI',
                            validators=[RegexValidator(regex=ISNI_REGEX, message=ISNI_V_MSG)])
    amazon_music_id = models.TextField(unique=True, blank=True, null=True, verbose_name='Amazon Music ID')
    ipis = models.ManyToManyField(Ipi, related_name="artist", through='ArtistIpis', through_fields=('artist', 'ipi'),
                                  verbose_name="IPIs")
    wikidata_id = models.TextField(unique=True, blank=True, null=True, verbose_name='Wikidata ID')

    class Meta:
        app_label = 'artists'
        managed = False
        db_table = 'artist'

    def __str__(self):
        return self.name


class ArtistGenres(models.Model):
    artist = models.OneToOneField(Artist, models.CASCADE, primary_key=True)
    genre = models.ForeignKey(Genre, models.CASCADE)

    class Meta:
        app_label = 'artists'
        managed = False
        db_table = 'artist_genres'
        unique_together = (('artist', 'genre'),)

    def __str__(self):
        return self.genre.name


class ArtistIpis(models.Model):
    artist = models.OneToOneField(Artist, models.CASCADE, primary_key=True)
    ipi = models.OneToOneField(Ipi, models.CASCADE)

    class Meta:
        app_label = 'artists'
        managed = False
        db_table = 'artist_ipis'
        unique_together = (('artist', 'ipi'),)


class Label(models.Model):
    name = models.TextField()
    formation_date = models.CharField(max_length=10, blank=True, null=True)
    formation_area = models.TextField(blank=True, null=True)
    formation_country = models.ForeignKey(Country, models.CASCADE)
    closing_date = models.CharField(max_length=10, blank=True, null=True)
    favourite = models.BooleanField()
    label_code = models.TextField(unique=True, blank=True, null=True)
    ipis = models.ManyToManyField(Ipi, related_name="label", through='LabelIpis', through_fields=('label', 'ipi'))
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'labels'
        managed = False
        db_table = 'label'

    def __str__(self):
        return self.name


class ReleaseStatus(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release_status'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.TextField(unique=True)
    colour = models.CharField(unique=True, max_length=7)

    class Meta:
        app_label = 'statuses'
        managed = False
        db_table = 'status'

    def __str__(self):
        return self.name


class ReleaseType(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release_type'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.TextField(unique=True)
    charset = models.TextField()
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'languages'
        managed = False
        db_table = 'language'

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.TextField()
    birth_date = models.CharField(max_length=10, blank=True, null=True)
    birth_area = models.TextField(blank=True, null=True)
    birth_country = models.ForeignKey(Country, models.CASCADE, related_name='birthCountry')
    death_date = models.CharField(max_length=10, blank=True, null=True)
    death_area = models.TextField(blank=True, null=True)
    death_country = models.ForeignKey(Country, models.CASCADE, blank=True, null=True, related_name='deathCountry')
    favourite = models.BooleanField()
    isni = models.CharField(unique=True, max_length=19, blank=True, null=True)
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'producers'
        managed = False
        db_table = 'producer'


class Release(models.Model):
    title = models.TextField()
    release_date = models.CharField(max_length=10)
    artists = models.ManyToManyField(Artist, related_name="release", through='ReleaseArtists',
                                     through_fields=('release', 'artist'))
    genres = models.ManyToManyField(Genre, related_name="release", through='ReleaseGenres',
                                    through_fields=('release', 'genre'))
    types = models.ManyToManyField(ReleaseType, related_name='release', through='ReleaseTypes',
                                   through_fields=('release', 'release_type'))
    total_tracks = models.SmallIntegerField()
    missing_tracks = models.SmallIntegerField()
    total_discs = models.SmallIntegerField()
    missing_discs = models.SmallIntegerField()
    favourite = models.BooleanField()
    languages = models.ManyToManyField(Language, related_name='release', through='ReleaseLanguages',
                                       through_fields=('release', 'language'))
    rym_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    aoty_rank = models.SmallIntegerField(blank=True, null=True)
    bea_rank = models.SmallIntegerField(blank=True, null=True)
    christgau_rating = models.TextField(blank=True, null=True)
    hull_rating = models.TextField(blank=True, null=True)
    scaruffi_rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    metacritic = models.SmallIntegerField(blank=True, null=True)
    pitchfork_rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    art_quality = models.SmallIntegerField()
    tag_quality = models.SmallIntegerField()
    bitrate = models.TextField()
    producers = models.ManyToManyField(Producer, related_name='release', through='ReleaseProducers',
                                       through_fields=('release', 'producer'))
    asin = models.CharField(unique=True, max_length=10, blank=True, null=True)
    wikidata_id = models.TextField(unique=True, blank=True, null=True)
    release_status = models.ForeignKey(ReleaseStatus, models.CASCADE)
    log_status = models.ForeignKey(Status, models.CASCADE)
    description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release'

    def __str__(self):
        return self.title


class Media(models.Model):
    name = models.TextField(unique=True)
    type = models.TextField()
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'media'
        managed = False
        db_table = 'media'


class CatalogueItems(models.Model):
    label = models.ForeignKey(Label, models.CASCADE)
    release = models.ForeignKey(Release, models.CASCADE, blank=True, null=True)
    catalogue_id = models.TextField()
    media = models.ManyToManyField(Media, related_name="catalogue", through='CatalogueMedia',
                                   through_fields=('global_catalogue', 'media'))
    release_status = models.ForeignKey(ReleaseStatus, models.CASCADE)

    class Meta:
        app_label = 'labels'
        managed = False
        db_table = 'catalogue_items'


class CatalogueMedia(models.Model):
    global_catalogue = models.OneToOneField(CatalogueItems, models.CASCADE, primary_key=True)
    media = models.ForeignKey(Media, models.CASCADE)

    class Meta:
        app_label = 'labels'
        managed = False
        db_table = 'catalogue_media'
        unique_together = (('global_catalogue', 'media'),)


class LabelIpis(models.Model):
    label = models.OneToOneField(Label, models.CASCADE, primary_key=True)
    ipi = models.OneToOneField(Ipi, models.CASCADE)

    class Meta:
        app_label = 'labels'
        managed = False
        db_table = 'label_ipis'
        unique_together = (('label', 'ipi'),)

    def __str__(self):
        return self.ipi.ipi_id


class ProducerIpis(models.Model):
    producer = models.OneToOneField(Producer, models.CASCADE, primary_key=True)
    ipi = models.OneToOneField(Ipi, models.CASCADE)

    class Meta:
        app_label = 'producers'
        managed = False
        db_table = 'producer_ipis'
        unique_together = (('producer', 'ipi'),)


class ReleaseArtists(models.Model):
    release = models.OneToOneField(Release, models.CASCADE, primary_key=True)
    artist = models.ForeignKey(Artist, models.CASCADE)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release_artists'
        unique_together = (('release', 'artist'),)


class ReleaseGenres(models.Model):
    release = models.OneToOneField(Release, models.CASCADE, primary_key=True)
    genre = models.ForeignKey(Genre, models.CASCADE)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release_genres'
        unique_together = (('release', 'genre'),)


class ReleaseLanguages(models.Model):
    release = models.OneToOneField(Release, models.CASCADE, primary_key=True)
    language = models.ForeignKey(Language, models.CASCADE)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release_languages'
        unique_together = (('release', 'language'),)


class ReleaseProducers(models.Model):
    release = models.OneToOneField(Release, models.CASCADE, primary_key=True)
    producer = models.ForeignKey(Producer, models.CASCADE)

    class Meta:
        app_label = 'releases'
        managed = False
        db_table = 'release_producers'
        unique_together = (('release', 'producer'),)


class ReleaseTypes(models.Model):
    release = models.OneToOneField(Release, models.CASCADE, primary_key=True)
    release_type = models.ForeignKey(ReleaseType, models.CASCADE)

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

    def __str__(self):
        return self.name


class Track(models.Model):
    title = models.TextField()
    track_type = models.ForeignKey(TrackType, models.CASCADE)
    artist = models.ForeignKey(Artist, models.CASCADE, related_name='artist')
    original_artist = models.ForeignKey(
        Artist, models.CASCADE, blank=True, null=True, related_name='originalArtist')
    favourite = models.BooleanField()
    wikidata_id = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        app_label = 'tracks'
        managed = False
        db_table = 'track'

    def __str__(self):
        return "{0} - {1}".format(self.title, self.artist.name)


class TrackIsrc(models.Model):
    isrc = models.CharField(primary_key=True, max_length=15)
    track = models.ForeignKey(Track, models.CASCADE, blank=True, null=True)

    class Meta:
        app_label = 'tracks'
        managed = False
        db_table = 'track_isrc'


class TrackIswc(models.Model):
    iswc = models.CharField(primary_key=True, max_length=15)
    track = models.ForeignKey(Track, models.CASCADE, blank=True, null=True)

    class Meta:
        app_label = 'tracks'
        managed = False
        db_table = 'track_iswc'
