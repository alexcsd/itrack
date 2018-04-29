from django.urls import path
from . import views 
app_name='article'
urlpatterns = [
    path('', views.article,name="home"),
    path('create/', views.create,name="create"),
    path('<slug>/', views.details,name="details"),

]
