#!/usr/bin/env python
import requests
import sys
import os

sys.path.append("..")  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from app.models import Artist, Album

albums = Album.objects.all()

print albums

# for album in albums:

try:
	# print album.id

	# artist_handle = album.artist_name

	# artist_handle = artist_handle.replace(' ', '_')

	# print artist_handle

	response = requests.get('https://freemusicarchive.org/api/get/artists.json?api_key=60BLHNQCAOUFPIBZ&limit=500') #artist_handle=%s' % artist_handle)

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

		# album.artist = artist
		# album.save()

except Exception, e:
	print e