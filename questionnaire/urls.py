from django.urls import path
from . import views

app_name = 'questionnaire'
urlpatterns = [
    path('',  views.welcome, name='welcome'),
    path('abet',  views.abet, name='abet'),
    path('questionnaire',  views.index, name='index'),
    path('questions',  views.view_questions, name='questions'),
    path('nextquestion',  views.next_question, name='next_question'),
]
