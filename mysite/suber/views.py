from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from suber.models import Suber

def index(request):
    last_recipient = Suber.objects.all()
    print len(last_recipient)
    context = {'last_recipient': last_recipient}
    print context
    return render(request, 'suber/index.html', context)

def index2(request):
	return render(request, 'suber/index_2.html')

def submit(request):
	if 'SenderName' in request.POST:
		sendername = request.POST['SenderName']
		sendermemo = request.GET['SenderMemo']
	print("...........Testing...........")
	return HttpResponse()