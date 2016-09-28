from django.conf.urls import url 
from . import views
from django.contrib import admin

app_name = 'Repertoire'

urlpatterns=[
# url(r'^$', views.index, name='index'),
# url(r'^AddSongPage', vie.ws.AddSongPage, name='AddSongPage'),
url(r'^$', views.Repertoire, name='Repertoire'),
url(r'^AddSong', views.AddSong, name='AddSong'),
# url(r'^MainPage', views.MainPage, name='MainPage'),
url(r'^Login', views.Login, name='Login' ),
url(r'^Logout', views.Logout, name='Logout'),

]
