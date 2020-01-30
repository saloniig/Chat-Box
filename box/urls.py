from django.urls import path
from . import views
from box.views import *
from django.views.generic import FormView

  
urlpatterns = [
    path('', AboutView.as_view()),
    path('sign/', email.as_view()),
    path('otp/', otp.as_view()),
    path('signup/', signup.as_view()),





  ]