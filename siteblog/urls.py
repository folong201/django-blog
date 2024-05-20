from django.http import HttpResponse

from django.urls import path

from . import views,moderatorviews,userviews,auth

urlpatterns = [ 
    path("",views.index,name="index"),
    path('moderator/', moderatorviews.index),
    path('user/', userviews.index),
    path('auth/login',auth.login_view,name="login"),
    path('auth/register',auth.register_view,name="register")
]

