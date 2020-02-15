from django.urls import path
from . import views
from django.conf.urls import url
from box.views import *
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required

  
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.index,name='index'),  
    path('topic',login_required(views.topics),name='topics'),
    path('log',views.log,name='log'),
    url(r'^search/$', views.Searchform, name='Search'),


  ]

  

