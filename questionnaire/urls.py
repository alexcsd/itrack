from django.urls import path
from . import views

app_name = 'questionnaire'
urlpatterns = [
    path('',  views.welcome, name='welcome'),
    path('result',  views.result, name='result'),
    path('about',  views.welcome, name='about'),
    path('questions',  views.question, name='questions'),
    path('questionfetch',  views.question_fetch, name='questionFetch'),
    path('questionfetch/<int:pk>',  views.question_fetch, name='questionFetch'),
    path('startcourse/<str:course>',  views.start_course, name='startcourse'),
    path('abet',  views.abet, name='abet'),
]
