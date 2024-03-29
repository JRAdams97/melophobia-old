# Generated by Django 4.1.2 on 2022-10-27 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('release_date', models.CharField(max_length=10)),
                ('total_tracks', models.SmallIntegerField()),
                ('missing_tracks', models.SmallIntegerField()),
                ('total_discs', models.SmallIntegerField()),
                ('missing_discs', models.SmallIntegerField()),
                ('favourite', models.BooleanField()),
                ('rym_rating', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('aoty_rank', models.SmallIntegerField(blank=True, null=True)),
                ('bea_rank', models.SmallIntegerField(blank=True, null=True)),
                ('christgau_rating', models.TextField(blank=True, null=True)),
                ('hull_rating', models.TextField(blank=True, null=True)),
                ('scaruffi_rating', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('metacritic', models.SmallIntegerField(blank=True, null=True)),
                ('pitchfork_rating', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('art_quality', models.SmallIntegerField()),
                ('tag_quality', models.SmallIntegerField()),
                ('bitrate', models.TextField()),
                ('asin', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('wikidata_id', models.TextField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'release',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReleaseStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'release_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReleaseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'release_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReleaseArtists',
            fields=[
                ('release', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='releases.release')),
            ],
            options={
                'db_table': 'release_artists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReleaseGenres',
            fields=[
                ('release', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='releases.release')),
            ],
            options={
                'db_table': 'release_genres',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReleaseLanguages',
            fields=[
                ('release', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='releases.release')),
            ],
            options={
                'db_table': 'release_languages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReleaseProducers',
            fields=[
                ('release', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='releases.release')),
            ],
            options={
                'db_table': 'release_producers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReleaseTypes',
            fields=[
                ('release', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='releases.release')),
            ],
            options={
                'db_table': 'release_types',
                'managed': False,
            },
        ),
    ]
