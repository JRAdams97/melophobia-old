# Generated by Django 4.1.2 on 2022-11-22 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ipi',
            options={'managed': False, 'verbose_name': 'IPI', 'verbose_name_plural': 'IPIs'},
        ),
    ]
