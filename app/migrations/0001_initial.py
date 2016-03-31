# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album_id', models.IntegerField(null=True, blank=True)),
                ('album_title', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_name', models.CharField(max_length=255, null=True, blank=True)),
                ('album_image', models.ImageField(null=True, upload_to=b'album_images', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist_id', models.IntegerField(null=True, blank=True)),
                ('artist_handle', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_name', models.CharField(max_length=255, null=True, blank=True)),
                ('artist_url', models.URLField(null=True, blank=True)),
                ('artist_image', models.ImageField(null=True, upload_to=b'artist_images', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre_id', models.IntegerField(null=True, blank=True)),
                ('genre_parent_id', models.IntegerField(null=True, blank=True)),
                ('genre_title', models.CharField(max_length=255, null=True, blank=True)),
                ('genre_handle', models.SlugField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('track_id', models.IntegerField(null=True, blank=True)),
                ('track_title', models.CharField(max_length=255, null=True, blank=True)),
                ('track_url', models.URLField(null=True, blank=True)),
                ('track_image_file', models.ImageField(null=True, upload_to=b'track_images', blank=True)),
                ('artist_id', models.IntegerField(null=True, blank=True)),
                ('album_id', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
