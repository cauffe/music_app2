from django.db import models

# Create your models here.
class Genre(models.Model):
	genre_id = models.IntegerField(null=True, blank=True)
	genre_parent_id = models.IntegerField(null=True, blank=True)
	genre_title = models.CharField(null=True, blank=True, max_length=255)
	genre_handle = models.SlugField(null=True, blank=True)

	def __unicode__(self):
		return '%s' % self.genre_title

class Artist(models.Model):
	artist_id = models.IntegerField(null=True, blank=True)
	artist_handle = models.CharField(null=True, blank=True, max_length=255)
	artist_name  = models.CharField(null=True, blank=True, max_length=255)
	artist_url = models.URLField(null=True, blank=True)
	artist_image = models.ImageField(null=True, blank=True, upload_to='artist_images')

	def __unicode__(self):
		return '%s' % self.artist_name

class Album(models.Model):
	album_id = models.IntegerField(null=True, blank=True)
	album_title = models.CharField(null=True, blank=True, max_length=255)
	artist_name = models.CharField(null=True, blank=True, max_length=255)
	album_image = models.ImageField(null=True, blank=True, upload_to='album_images')
	artist = models.ForeignKey('app.Artist', null=True, blank=True)

	def __unicode__(self):
		return '%s' % self.album_title

class Track(models.Model):
	track_id = models.IntegerField(null=True, blank=True)
	track_title = models.CharField(null=True, blank=True, max_length=255)
	track_url = models.URLField(null=True, blank=True)
	track_image_file = models.ImageField(null=True, blank=True, upload_to='track_images')
	artist_id = models.IntegerField(null=True, blank=True)
	album_id = models.IntegerField(null=True, blank=True)




