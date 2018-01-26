from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.core.files.storage import FileSystemStorage
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
	return render(request,'users/profile.html')

def signup_view(request):
	if request.method== 'GET':
		return redirect('/')
	if request.method== 'POST':
		register_form=UserCreationForm(request.POST)
		if register_form.is_valid():
			user=register_form.save()
			login(request,user)

			return redirect('/')

	return render(request,'main/index.html',{'register_form':register_form})

def login_view(request):
	if request.method== 'GET':
		return redirect('/')
	if request.method=='POST':
		login_form=AuthenticationForm(data=request.POST)
		if login_form.is_valid():
			#log em in
			user=login_form.get_user()
			login(request,user)
			return redirect('/')
	else:
		login_form=AuthenticationForm()

	return render(request,'main/index.html',{'login_form':login_form})

def logout_view(request):
	logout(request)
	return redirect('/')
