from django.shortcuts import render

# AEttinger 7.2.15 - added to view http content.
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello world!")