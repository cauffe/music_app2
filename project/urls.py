from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^artist_list/$', 'app.views.artist_list'),
    url(r'^artist_detail/(?P<pk>.+)/$', 'app.views.artist_detail'),

    url(r'^album_list/$', 'app.views.album_list'),
    url(r'^album_detail/(?P<pk>.+)/$', 'app.views.album_detail'),

    url(r'^signup/$', 'app.views.sign_up'),
    url(r'^logout/$', 'app.views.logout_view'),
    url(r'^signin/$', 'app.views.login_view'),
    url(r'^create_album/$', 'app.views.create_album'),
    url(r'^edit_album/(?P<pk>.+)/$', 'app.views.edit_album'),

    url(r'^delete_album/(?P<pk>.+)/$', 'app.views.delete_album'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
