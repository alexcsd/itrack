'''
handles all the course watching logic and templates
'''

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import Profile
from .models import Course

@login_required
def watch(request, index):
    '''
    retrives the course from the databse, and returns it's link
    '''
    #course links
    course = request.user.profile.course
    links = course.links.split(';')
    #current index link
    current_link = links[index-1]
    ctx = {
        'course_title':course.title,
        'links':links,
        'current_link':current_link
    }
    return render(request, 'watch_course/watch.html', ctx)
