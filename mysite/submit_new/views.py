from django.shortcuts import render

# Create your views here.
from suber.models import Suber

# Create your views here.
def index(request):
    return render(request, 'submit_new/index.html')