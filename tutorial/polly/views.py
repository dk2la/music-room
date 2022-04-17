from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
# from django.template import loader

from . import models

# Create your views here.
def index(request):
    latest_questions_list = models.Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_questions_list])
    # template = loader.get_template('polly/index.html')
    context = {'latest_question_list' : latest_questions_list}
    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))
    return render(request, 'polly/index.html', context)

def details(request, question_id):
    # try:
    #     question = models.Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("Have no question")

    question = get_object_or_404(models.Question, pk=question_id)
    return render(request, 'polly/details.html', {'question': question})

def result(request, question_id):
    return HttpResponse("Answer for question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You are voted for question %s." % question_id)

