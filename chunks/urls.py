from django.conf.urls import patterns, url

from chunks import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<day>\d+)/(?P<month>\d+)/(?P<year>\d+)/(?P<hour>\d+)/(?P<minute>\d+)/$', views.chunk_details, name='chunk_details'),
    url(r'^(?P<day>\d+)/(?P<month>\d+)/(?P<year>\d+)/(?P<hour>\d+)/(?P<minute>\d+)/gather=(?P<gather_amount>\d+)$', views.chunk_gather, name='chunk_gather'),
)
