#!/usr/bin/env python
import requests
import sys
import os

sys.path.append("..")  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from app.models import Album
import django
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

django.setup()

response = requests.get('https://freemusicarchive.org/api/get/albums.json?api_key=60BLHNQCAOUFPIBZ&limit=500')

response_dict = response.json()

for data in response_dict['dataset']:

    album, created = Album.objects.get_or_create(album_title=data['album_title'])

    album.album_id = data['album_id']
    album.artist_name = data['artist_name']

    try:
        album_image = requests.get(data['album_image_file'])

        # print album_image.content

        temp_image = NamedTemporaryFile(delete=True)

        temp_image.write(album_image.content)

        album.album_image = File(temp_image)

        print album.album_title

    except Exception, e:
        print e

    album.save()
