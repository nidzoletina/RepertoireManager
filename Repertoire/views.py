from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import song
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
	SongsInRepertoire = song.objects.all().order_by('name')
	return render(request, 'Repertoire/repertoire.html', { 'songs' : SongsInRepertoire} )

# def check(request):
# 	return HttpResponse("Check")
# @login_required()
def Repertoire(request):
	# if not request.user_is_authenticated:
	# 	return HttpResponse("Page Not Found")

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
	return HttpResponseRedirect(reverse("Repertoire:index"))

# 	a = AddSongPage(request)
# 	return a