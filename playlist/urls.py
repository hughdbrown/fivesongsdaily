from django.conf.urls.defaults import *
from django.contrib.comments.models import Comment
from django.views.generic.simple import direct_to_template

from fivesongsdaily.playlist import views

urlpatterns = patterns('',
    url(r'^preview/(?P<id>\w+)/$',	    views.preview_id,	        name='playlist_previewbyid'),

    url(r'^id/(?P<id>\w+)/$',		    views.show_id,		        name='playlist_byid'),
    url(r'^all/$',			            views.show_all,		        name='playlist_all'),

    url(r'^song/add/$',		            views.user_song_upload,	    name='playlist_song_upload'),
    url(r'^upload/(?P<message>.+)/$',	views.user_playlist,	    name='playlist_save'),
    url(r'^upload/$',			        views.user_playlist,	{'message':None},    name='playlist_save'),

    url(r'^(?P<id>\w+)/$',		        views.show_id,		        name='playlist_byid'),
    url(r'^$',				            views.show_home,	        name='playlist_home'),
)
