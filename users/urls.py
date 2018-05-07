from django.urls import path
from . import views
from .views import *

app_name = 'user'

urlpatterns=[
path('signup/',SignupView.as_view(),name="signup"),
path('login/',LoginView.as_view(),name="signin"),
path('logout/',views.logout_view,name="logout"),
path('profile/',views.current_profile,name="cprofile"),
path('profile/<slug:username>/',views.profile_view,name="profile"),
path('profile/setting',views.setting,name="setting"),
path('profile/changeprofile',views.change_profile,name="change_profile"),
path('profile/changesecurity',views.change_security,name="change_security"),
]
