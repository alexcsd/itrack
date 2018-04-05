from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import Profile
#from .models import
# Create your views here.
@login_required
def watch(request):
    user_profile=request.user.profile
    user_course_links=user_profile.course.links
    index=user_profile.course_index
    link=user_course_links.split(';')[index]

    return render(request, 'watch_course/watch.html',{'link':link})
