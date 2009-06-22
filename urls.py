from django.conf.urls.defaults import *
from django.contrib import admin
# import django.contrib.auth.views

from fivesongsdaily.settings import MEDIA_ROOT

from fivesongsdaily.feeds import LatestPlaylists

admin.autodiscover()

feeds = {
    'all': LatestPlaylists,
}

urlpatterns = patterns('',
    (r'^admin/r/10/(?P<id>\w+)/*$', 'fivesongsdaily.playlist.views.preview_id'),
    (r'^admin/(.*)', admin.site.root),

    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^comments/post/', include('django.contrib.comments.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

    (r'^password_reset/$', 'django.contrib.auth.views.password_reset'),
    (r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    (r'^profile/', include('fivesongsdaily.profiles.urls')),
    (r'^playlist/', include('fivesongsdaily.playlist.urls')),
    (r'^messages/', include('fivesongsdaily.message.urls')),
    (r'^pages/', include('fivesongsdaily.pages.urls')),
    (r'^contact/', include('fivesongsdaily.contact.urls')),
    (r'', include('fivesongsdaily.playlist.urls')),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

