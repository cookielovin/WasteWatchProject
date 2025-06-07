app_name = "base"

from django.urls import path
from . import views


urlpatterns = [

    path('home/', views.home, name='home'),
    path('login/', views.signin_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('createreport/', views.createreport_view, name='createreport')
]