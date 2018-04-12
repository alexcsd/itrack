'''
this module contains all the urls for the whole project
'''

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    path('watch/', include('watch_course.urls', namespace='watch')),
    # path('', RedirectView.as_view(url='/questionnaire/')),
    path('',  include('questionnaire.urls',namespace='questionnaire')),
    path('users/', include('users.urls',namespace='user')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
