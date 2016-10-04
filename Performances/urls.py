from django.conf.urls import url 
from . import views

app_name = 'Performances'

urlpatterns=[
# url(r'^$', views.index, name='index'),
# url(r'^AddSongPage', vie.ws.AddSongPage, name='AddSongPage'),
url(r'test', views.test, name="test"),
url(r'^', views.Performances, name='Performances'),
# url(r'^AddSong', views.AddSong, name='AddSong'),
# url(r'^MainPage', views.MainPage, name='MainPage'),
# url(r'^Login', views.Login, name='Login' ),
# url(r'^Logout', views.Logout, name='Logout'),

]
