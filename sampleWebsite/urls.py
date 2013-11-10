from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

SUBURL = ''

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sampleWebsite.views.home', name='home'),
    url(r'^ben/$', 'sampleWebsite.views.index_ben', name='index_ben'),
    url(r'^justin/$', 'sampleWebsite.views.index_justin', name='index_justin'),
    url(r'^abby/$', 'sampleWebsite.views.index_abby', name='index_abby'),
    
)

urlpatterns += staticfiles_urlpatterns()
