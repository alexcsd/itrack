from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.views.generic.edit import FormView

login_form=AuthenticationForm()
register_form=UserCreationForm()
context = {
    'register_form': register_form,
    'login_form': login_form
    }

def current_profile(request):
	if request.user.is_authenticated:
		return redirect('user:profile',request.user.username)
	return redirect('questionnaire:welcome')
def profile_view(request, username):
	global context
	context.update({'user_profile':username})
	return render(request,'users/profile/profile.html', context)

class SignupView(FormView):
	template_name='users/register.html'
	form_class=UserCreationForm
	def form_valid(self,form):
		user=form.save()
		login(self.request,user,backend='django.contrib.auth.backends.ModelBackend')
		return redirect('user:profile',user.username)

class LoginView(FormView):
	template_name='users/login.html'
	form_class=AuthenticationForm
	def form_valid(self,form):
		user=form.get_user()
		login(self.request,user,backend='django.contrib.auth.backends.ModelBackend')
		return redirect('user:profile',user.username)


def logout_view(request):
	logout(request)
	return redirect('questionnaire:welcome')
