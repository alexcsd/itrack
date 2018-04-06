from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Skill, Question, Answer
from django.core import serializers
from .utils import matrix
from django.views.decorators.csrf import csrf_protect
import logging
from numpy import array,matmul

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
    return render(request, 'questionnaire/questions.html', context)


@csrf_protect
def question_fetch(request,pk = None):
    if pk == None:
        next_question = Question.objects.order_by('pk').first()
        request.session['questions_meta'] ={
            'skills_vector':{
                'Logic':0,
                'Management':0,
                'People':0,
                'Mechanical':0,
                'Communication':0,
                'Judgment':0,
                'Attention':0,
                'Thinking':0,
            },
            'current_question_id':next_question.pk
        }
    else:
        if pk != 0:
            answer = Answer.objects.get(pk=pk)
            #logic = logic answer.weight/logic.question.count
            request.session['questions_meta']['skills_vector'][answer.Question.Skill.title] += answer.weight/answer.Question.Skill.question_set.count()
        #get next object
        try:
            next_question = Question.objects.all().filter(pk__gt=request.session['questions_meta']['current_question_id']).order_by('pk')[0:1]
            next_question = Question.objects.get(pk=next_question[0].pk)
            request.session['questions_meta']['current_question_id'] = next_question.pk
        except IndexError:
            return JsonResponse({'response':'200 ok'})
        #calculate
    ctx = {
        'question':next_question.body,
        'answers':serializers.serialize('json',next_question.answer_set.all()),
        'type':next_question.qtype
        }
    request.session.save()
    return JsonResponse(ctx)

def skills_mapping(request):
    logger = logging.getLogger(__name__)
    eight_skills_vector=request.session['questions_meta']['skills_vector']
    #alias so its shorter
    esv=eight_skills_vector
    #now its a list
    esv=[esv[i] for i in esv]
    esv=array(esv)
    d={     'logic':[1,0,1,0,1,1,0,0,1,0,1],
            'management':[0,1,0,1,0,0,0,0,0,0,1],
            'interaction':[0,0,0,1,0,0,1,1,0,1,0],
            'mechanical':[0,1,0,0,1,0,1,0,0,0,1],
            'communication':[0,0,0,1,0,1,1,1,1,1,0],
            'judgement':[0,0,0,0,1,0,0,0,0,0,0],
            'attention':[1,0,1,1,1,0,1,0,0,1,0],
            'thinking':[1,1,1,0,0,1,0,0,0,0,1]
            }
    eight_to_abet=[d[i] for i in d]
    eight_to_abet=array(eight_to_abet)
    abet_result=list(matmul(esv,eight_to_abet))
    logger.error(abet_result)
    return HttpResponse(' '.join([str(int(i)) for i in abet_result]))