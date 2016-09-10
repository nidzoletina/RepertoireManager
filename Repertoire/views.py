from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello World")

def check(request):
	return HttpResponse("Check")

def Repertoire(request):
	return render(request, 'Repertoire/repertoire.html' )

def PageNotFound(request):
	return HttpResponse("Page Not Found")