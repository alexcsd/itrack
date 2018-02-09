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
def profile_view(request, username):
	global context
	context.update({'user_profile':username})
	return render(request,'users/profile.html', context)

#we need to redirect back with errors 
class SignupView(FormView):
	template_name='questionnaire/index.html'#we don't have a specific template for sign up to show ; it's in all pages
	form_class=UserCreationForm
	success_url='/'
	def form_valid(self,form):
		user=form.save()
		login(self.request,user)
		return redirect('/') #use namespaces ex: redirect('user:profile')
	def form_invalid(self,form):
		return render(self.request,'questionnaire/index.html',{'register_form':form, 'login_form':login_form})

#same as Signup
class LoginView(FormView):
	template_name='questionnaire/index.html'
	form_class=AuthenticationForm
	success_url='/'
	def form_valid(self,form):
		user=form.get_user()
		login(self.request,user)
		return redirect('/')
	def form_invalid(self,form):
		return render(self.request,'questionnaire/index.html',{'login_form':form, 'register_form':register_form})


def logout_view(request):
	logout(request)
	return redirect('questionnaire:welcome')
