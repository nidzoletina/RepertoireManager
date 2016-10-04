from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Performance, SongOrder
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# def Performances(request):
# 	return HttpResponse("Yeeeey")

def Performances(request):
	if request.user.is_authenticated():
		# CurrentSelection = Performance.objects.get(pk=2)
		Performances = Performance.objects.all().order_by('date')
		CurrentSelection = Performances[0]
		Songs = SongOrder.objects.filter(performance=2).order_by('orderInPerformance')
		# Songs = SongOrder.objects.all()
		return render(request, 'Performances/Performances.html', { 'username' : request.user, 'loggedin' : True, 'Performances' : Performances, 'Songs' : Songs, 'CurrentSelection': CurrentSelection} )
	else:
		return render(request, 'Performances/Performances.html', { 'username': request.user, 'loggedin' : False } )

def test(request):
	return HttpResponse("Yeeeey")