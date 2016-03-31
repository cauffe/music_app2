#!/usr/bin/env python
import requests
import sys
import os

sys.path.append("..")  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from app.models import Genre  

response = requests.get('https://freemusicarchive.org/api/get/genres.json?api_key=60BLHNQCAOUFPIBZ&limit=100')

response_dict = response.json()

# print response_dict.keys()

# print response_dict['dataset']

for data in response_dict['dataset']:
	# print data.keys()
	genre, created = Genre.objects.get_or_create(genre_title=data['genre_title'])
	print created
	print genre

	genre.genre_id = data['genre_id']
	genre.genre_handle = data['genre_handle']
	genre.genre_parent_id = data['genre_parent_id']

	genre.save()

	# print data['genre_title']
	# print data['genre_parent_id']
	# print data['genre_handle']
	# print data['genre_id']

# print response_dict

# print response_dict.json()