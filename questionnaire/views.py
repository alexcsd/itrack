from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Question


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


def view_questions(request):
    question = Question.objects.get(pk=1)
    global context
    context.update({'question':question})
    return render(request, 'questionnaire/questions.html', context)

def next_question(request):
    id = request.GET['answer']
    if id.isdigit():
        question = Question.objects.get(pk=id)
        context.update({'question':question})
        return render(request, 'questionnaire/questions.html', context)

    else:
        context.update({'recommended':id})
        return render(request, 'questionnaire/recommended.html', context)
