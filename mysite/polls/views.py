from django.shortcuts import render

from polls.models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()
    print len(latest_question_list)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
