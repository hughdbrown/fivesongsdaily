from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('django.views.generic.simple',
    url(regex=r'^about/$',	view='direct_to_template', kwargs={'template': 'about.html'}, name="about"),
    url(regex=r'^$',		view='direct_to_template', kwargs={'template': 'about.html'}, name="about"),
)

