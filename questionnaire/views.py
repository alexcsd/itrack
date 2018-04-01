from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Skill, Question, Answer
from django.core import serializers

# Create your views here.
register_form = UserCreationForm()
login_form = AuthenticationForm()
context = {
    'register_form': register_form,
    'login_form': login_form
    }

def abet(request):
    from . import abet
    if request.method=='POST':
        answers_vector=request.POST['vector']
        best_subject=abet.get_track( answers_vector.split(','))
        #return render(request,'questionnaire/abet.html',{'subject':best_subject})
        context.update({'recommended':best_subject})
        return render(request, 'questionnaire/recommended.html', context)
    return render(request,'questionnaire/abet.html',context)

def welcome(request):
    return render(request,'questionnaire/welcome.html',context)

def index(request):
    return render(request, 'questionnaire/index.html', context)

def result(request):
    return render(request, 'questionnaire/result.html', context)


def question(request):
    global context
    context.update({
        'skills':Skill.objects.all(),
    })
    return render(request, 'questionnaire/questions.html', context)

def question_fetch(request):
    ctxt = {
        'skills':Skill.objects.all().get()
    }
    objs =Skill.objects.all()
    jsondata = serializers.serialize('json', ctxt)
    return HttpResponse(jsondata, content_type='application/json')
