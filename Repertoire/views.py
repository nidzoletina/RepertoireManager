from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import song
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def Repertoire(request):
	if request.user.is_authenticated():		
		SongsInRepertoire = song.objects.all().order_by('name')
		return render(request, 'Repertoire/repertoire.html', { 'username' : request.user, 'loggedin' : True, 'songs' : SongsInRepertoire} )
	else:
		return render(request, 'Repertoire/repertoire.html', { 'username': request.user, 'loggedin' : False } )
  	
def Login(request):	
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
	return HttpResponseRedirect(reverse("Repertoire:Repertoire"))

def Logout(request):
	logout(request)
	return HttpResponseRedirect(reverse("Repertoire:Repertoire"))

def AddSong(request):
	s = song(name=request.POST['SongName'])
	s.save()
	return HttpResponseRedirect(reverse("Repertoire:Repertoire"))