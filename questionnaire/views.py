'''
handles all the questionnaire and main page logic
'''

from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Skill, Question, Answer
from watch_course.models import Course
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
import logging
from numpy import array,matmul
from random import randint

# Create your views here.
register_form = UserCreationForm()
login_form = AuthenticationForm()
context = {
    'register_form': register_form,
    'login_form': login_form
    }

def abet(request):
    '''
    an unused function, was an initial idea that we discarded
    was based on intersecting the abest skills vector [1,0,..k=11]
    with an outcome matrix, and returning maximum intersction count
    '''
    from . import abet
    if request.method=='POST':
        answers_vector=request.POST['vector']
        best_subject=abet.get_track( answers_vector.split(','))
        #return render(request,'questionnaire/abet.html',{'subject':best_subject})
        context.update({'recommended':best_subject})
        return render(request, 'questionnaire/recommended.html', context)
    return render(request,'questionnaire/abet.html',context)

def welcome(request):
    '''
    this one and the following functions are obvious
    '''
    return render(request,'questionnaire/welcome.html',context)

def index(request):
    return render(request, 'questionnaire/index.html', context)

def question(request):
    if request.user.is_authenticated:
        global context
        context.update({'hasACourse':True if request.user.profile.course else False})
    return render(request, 'questionnaire/questions.html', context)


@csrf_protect
def question_fetch(request,pk = None):
    '''
    an important view
    retrives questions from the database, displays them in the template
    and more importantly, keeps track of the skills vectors in the session
    '''
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

def result(request):
    '''
    does all the mapping from skill vectors to courses
    uses numpy to do matrix multiplication
    the metric used is the inner product
    '''
    if 'questions_meta' not in request.session:
        return redirect('/')
    logger = logging.getLogger(__name__)
    eight_skills_vector=request.session['questions_meta']['skills_vector']
    #alias so its shorter
    esv=eight_skills_vector
    #now its a list
    esv=[esv[i] for i in esv]
    esv=array(esv)
    skills_matrix={
        'logic':[1,0,1,0,1,1,0,0,1,0,1],
        'management':[0,1,0,1,0,0,0,0,0,0,1],
        'interaction':[0,0,0,1,0,0,1,1,0,1,0],
        'mechanical':[0,1,0,0,1,0,1,0,0,0,1],
        'communication':[0,0,0,1,0,1,1,1,1,1,0],
        'judgement':[0,0,0,0,1,0,0,0,0,0,0],
        'attention':[1,0,1,1,1,0,1,0,0,1,0],
        'thinking':[1,1,1,0,0,1,0,0,0,0,1]
    }
    eight_to_abet=[skills_matrix[i] for i in skills_matrix]
    eight_to_abet=array(eight_to_abet)
    esv=esv.reshape(1,8)
    abet_result=list(matmul(esv,eight_to_abet))
    subject_matrix=[
        [1,1,1,0,1,0,0,0,1,1,1],
        [1,1,1,0,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0],
        [randint(0,1) for i in range(11)],
        [1,1,1,1,1,1,0,1,1,1,0],
        [randint(0,1) for i in range(11)],
        [1,0,1,1,1,0,0,1,1,0,1],
        [randint(0,1) for i in range(11)],
        [randint(0,1) for i in range(11)],
        [randint(0,1) for i in range(11)],
        [randint(0,1) for i in range(11)],
        [1,1,1,0,1,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,0,1,0,0,0,1,0,1]
    ]
    subject_names=[
        'Artificial Intellegence',
        'Advanced datastructures',
        'Intro to algorithms',
        'Advanced algorithms',
        'Computer Security',
        'Mathematics for computer science',
        'Computer Graphics',
        'Neural network',
        'Data analysis',
        'Data visualization',
        'Intro to CS and programming',
        'Operating Systems',
        'Machine Learning',
        'Database systems',
    ]
    subject_matrix=array(subject_matrix)
    #shape (n*11)
    #to be consistent, we'll transpose
    subject_matrix=subject_matrix.T
    subject_results_vector=matmul(abet_result,subject_matrix)
    #alias
    srv=subject_results_vector
    srv=srv.tolist()[0]
    top_three_courses = sorted(zip(srv, subject_names), reverse=True)[:3]
    context.update({'courses':top_three_courses})
    #delete session
    # del request.session['questions_meta'] #commented for testing purposes
    return render(request, 'questionnaire/result.html', context)

def start_course(request, course):
    '''
    Saves and displays the course to the user
    '''
    if request.user.is_authenticated:
        if request.user.profile.course:
            #uncomment the following line after finishing our database
            _course = Course.objects.get(title=course)
            # _course = Course.objects.get(title='Advanced data structures')
            request.user.profile.course = _course
            request.user.profile.course_index=0
            request.user.profile.save()
            return redirect('watch_course:watch',index=1)
    #save course in a session
    request.session['result'] = course
    request.session.save()
    #redirect to registration page and save the course while registration
    return redirect('user:signup')
