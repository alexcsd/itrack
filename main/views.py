from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def index(request):
    register_form = UserCreationForm()
    login_form=AuthenticationForm()
    return render(request,'main/index.html',{
    'register_form':register_form,
    'login_form':login_form
    })
