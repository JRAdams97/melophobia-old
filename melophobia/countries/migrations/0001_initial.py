# Generated by Django 4.1.2 on 2022-10-27 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('wikidata_id', models.TextField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
    ]