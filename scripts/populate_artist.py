#!/usr/bin/env python
import requests
import sys
import os

sys.path.append("..")  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from app.models import Artist  

response = requests.get('https://freemusicarchive.org/api/get/artists.json?api_key=60BLHNQCAOUFPIBZ&limit=500')

response_dict = response.json()

for data in response_dict['dataset']:
	# print data.keys()
	# print '------'

	artist, created = Artist.objects.get_or_create(artist_name=data['artist_name'])
	artist.artist_handle = data['artist_handle']
	artist.artist_id = data['artist_id']
	artist.artist_url = data['artist_url']

	artist.save()

	print artist
	print created