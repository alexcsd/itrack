'''
handles all the user registeration-authentication-profiling
'''
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
	''' 
	checks if the user is logged in, if he's logged in it redirects to his profile,
	if he's not logged in it redirects to the main page
	'''
	if request.user.is_authenticated:
		return redirect('user:profile',request.user.username)
	return redirect('questionnaire:welcome')

def profile_view(request, username):
	'''
	updates the template context with the username, and displays his profile
	'''
	global context
	context.update({'user_profile':username})
	return render(request,'users/profile/profile.html', context)

class SignupView(FormView):
	''' class-based view (Generic views)
	handles the user registeration, and initializes the course counter to 0
	'''
	template_name='users/register.html'
	form_class=UserCreationForm
	def form_valid(self,form):
		user=form.save()
		if request.session['course']:
			_course = Course.objects.get(title=request.session['course'])
			self.request.user.profile.course = _course
			self.request.user.profile.course_index=0
			self.request.user.profile.save()
			del self.request.session['course']
		login(self.request,user,backend='django.contrib.auth.backends.ModelBackend')
		return redirect('user:profile',user.username)

class LoginView(FormView):
	'''
    class-based view

    logs the user in if the information is correct
    '''
	template_name='users/login.html'
	form_class=AuthenticationForm
	def form_valid(self,form):
		user=form.get_user()
		login(self.request,user,backend='django.contrib.auth.backends.ModelBackend')
		return redirect('user:profile',user.username)


def logout_view(request):
	'''
    logs the user out
    '''
	logout(request)
	return redirect('questionnaire:welcome')
