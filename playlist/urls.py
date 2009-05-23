from django.conf.urls.defaults import *
from django.contrib.comments.models import Comment
from django.views.generic.simple import direct_to_template

from fivesongs.playlist import views

urlpatterns = patterns('',
    url(r'^id/(?P<id>\w+)/*$',      views.show_id,	name='playlist_byid'),
    url(r'^all/*$',		    views.show_all,     name='playlist_all'),
    url(r'^(?P<id>\w+)/*$',      views.show_id,      name='playlist_byid'),
    url(r'^$',			    views.show_home,    name='playlist_home'),
)
