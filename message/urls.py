from django.conf.urls.defaults import *

from fivesongsdaily.message import views

urlpatterns = patterns('',
    url(r'^$',                      views.show_all,        name='messages_all'),
)

