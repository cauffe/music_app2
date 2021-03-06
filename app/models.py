from django.db import models

from django.utils import timezone
from django.utils.http import urlquote
from django.core.mail import send_mail

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()

        if not email:
            raise ValueError('Email must be set')

        email = self.normalize_email(email)

        user = self.model(email=email,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now,
                          **extra_fields
                        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=255, blank=True, null=True)
    last_name = models.CharField('last name', max_length=255, blank=True, null=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=False)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    objects = CustomUserManager()

    fav_artists = models.ManyToManyField('app.Artist')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return '/users/%s' % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject,message,from_email, [self.email])


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




