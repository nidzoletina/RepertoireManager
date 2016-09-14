from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import song
# Create your views here.



def index(request):
	return HttpResponse("Hello World")

# def check(request):
# 	return HttpResponse("Check")

def Repertoire(request):
	SongsInRepertoire = song.objects.all().order_by('name')
	return render(request, 'Repertoire/repertoire.html', { 'songs' : SongsInRepertoire} )

def AddSongPage(request):
	return render(request, 'Repertoire/AddSong.html' )

def PageNotFound(request):
	# raise Http404("Page Not Found")
	return HttpResponse("Page Not Found")

def AddSong(request):
	s = song(name=request.POST['SongName'])
	s.save()

	a = AddSongPage(request)
	return a