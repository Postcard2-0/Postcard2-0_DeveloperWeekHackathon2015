from django.shortcuts import render

# AEttinger 7.2.15 6:20 pm - add to render database context
from submit.models import recipient

# AEttinger 7.2.15 - added to view http content. 6:20 pm commented out
from django.http import HttpResponse

from django.template import loader, Context

# Create your views here.

# def index(request):
# 	return HttpResponse("Hello world!")

def index(request):
	last_recipient = recipient.objects.all()
	context = { 'last_recipient:' : last_recipient }
	return render(request, 'submit/index.html', context)

# for testing:
def hello(request):
	return HttpResponse("Hello World!")

def view_data(request):
	l = recipient.objects.all()
	context = {'ID:' : l.id,
				'name': l.name,
				'street': l.recipient_street_text,
				'street_nr': l.recipient_street_nr,
				'city': l.recipient_city_text,
				'zip': l.recipient_city_zip,
				'country': l.recipient_country_text
				}
	for k in l:
		print(k.name)
	
	return render(request, 'submit/index.html', context)
