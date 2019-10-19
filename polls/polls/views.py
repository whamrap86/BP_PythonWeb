from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id)))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ',<br>'.join([q.question_text   for q in latest_question_list])
    content = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', content)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    content = {'question' : question}
    return render(request, 'polls/detail.html', content)


def retsults(request, question_id):
    question = get_object_or_404(Choice, pk=question_id)
    content = {'question':question}
    return render(request, 'polls/result.html', content)