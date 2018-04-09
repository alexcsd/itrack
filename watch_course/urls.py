from django.urls import path
from . import views

app_name = 'watch_course'
urlpatterns = [
    path('<int:index>/',  views.watch, name='watch'),
]
