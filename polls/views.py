from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("you're looking at question %s" % question_id)

def results(request, question_id):
    return HttpResponse("You're looking at results of question %s" % question_id)
    
def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
    