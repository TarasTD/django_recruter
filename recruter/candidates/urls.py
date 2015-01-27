from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
	url(r'^profile/(.+_.+)/edit/$', edit_profile),
    url(r'^profile/(.+_.+)/$', profile_view),
	url(r'^search/$', search),
	url(r'^index$', index),
	)

