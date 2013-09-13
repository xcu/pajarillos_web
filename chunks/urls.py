from django.conf.urls import patterns, url

from chunks import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^s=(?P<sdate>\d+-\d+-\d+-\d+-\d+)$', views.chunk_details, name='chunk_details'),
    url(r'^s=(?P<sdate>\d+-\d+-\d+-\d+-\d+)/e=(?P<edate>\d+-\d+-\d+-\d+-\d+)$', views.chunk_range, name='chunk_range'),
    #url(r'^(?P<day>\d+)/(?P<month>\d+)/(?P<year>\d+)/(?P<hour>\d+)/(?P<minute>\d+)/(?P<gather_amount>\d*)$', views.chunk_details, name='chunk_details'),
)
