from django.conf.urls import url 
from . import views

app_name = 'Repertoire'

urlpatterns=[
url(r'^$', views.index, name='index'),
# url(r'^AddSongPage', views.AddSongPage, name='AddSongPage'),
url(r'^AddSong', views.AddSong, name='AddSong'),
# url(r'^check$', views.check, name='check'),
# url(r'^$', views.PageNotFound, name='PageNotFound'),
]
