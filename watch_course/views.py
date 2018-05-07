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
    # index = 90
    if not index ==1:
        prev_index = index-1
    else:
        prev_index = False
    if len(links) >= index+1:
        next_index = index+1
        if request.user.profile.course_index < index:
            request.user.profile.course_index = index
            request.user.profile.save()
        progress = (request.user.profile.course_index-1)/len(links)*100
    else:
        next_index = False
        progress = 100
    ctx = {
        'course_title':course.title,
        'links':links,
        'current_link':current_link,
        'next_index': next_index,
        'prev_index': prev_index,
        'progress': progress
    }
    return render(request, 'watch_course/watch.html', ctx)
