from django.shortcuts import render

# Create your views here.
from suber.models import Suber

def index(request):
    last_recipient = Suber.objects.all()
    print len(last_recipient)
    context = {'last_recipient': last_recipient}
    print context
    return render(request, 'suber/index.html', context)
