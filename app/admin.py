from django.contrib import admin

from app.models import *
# Register your models here.

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(CustomUser)