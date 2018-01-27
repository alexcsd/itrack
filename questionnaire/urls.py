from django.urls import path
from . import views

urlpatterns = [
    path('',  views.questionnaire, name='questionnaire'),
    path('questions',  views.view_questions, name='questions'),
    path('nextquestion',  views.next_question, name='next_question'),


]
