from django.conf.urls import url 
from . import views


urlpatterns=[
url(r'^$', views.Repertoire, name='index'),
# url(r'^check$', views.check, name='check'),
# url(r'^$', views.PageNotFound, name='PageNotFound'),
]
