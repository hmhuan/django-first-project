from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question

# Create your views here.


def index(request):
    last_question_list = Question.objects.order_by('-pub_at')[:5]
    last_question_list = list(last_question_list)
    last_question_list.reverse()
    context = {'last_question_list': last_question_list}
    return render(request, 'polls/index.html', context)
    pass


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    pass


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
    pass


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
    pass
