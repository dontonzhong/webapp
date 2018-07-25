# Packges and what they do
from django.shortcuts import render #Easier code
from django.http import HttpResponse #Respond to requests
from django.http import Http404 #Throw exception
from django.template import loader #Loading a template
from .models import Question #Model


def index(request):
    return HttpResponse("Hello, World. You're at the polls index.")

def detail(request, question_id):
    try:
        question = Question.obects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request, 'polls/index.html', context)
