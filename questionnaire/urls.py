from django.urls import path
from . import views

app_name = 'questionnaire'
urlpatterns = [
    path('',  views.welcome, name='welcome'),
    path('result',  views.result, name='result'),
    path('about',  views.welcome, name='about'),
    path('questionnaire',  views.index, name='index'),
    path('questions',  views.question, name='questions'),
    path('questionfetch',  views.question_fetch, name='questionFetch'),
    path('questionfetch/<int:pk>',  views.question_fetch, name='questionFetch'),
    #map prints the skill vector
    path('map',  views.skills_mapping, name='map'),
    path('abet',  views.abet, name='abet'),
]
