from django.urls import path
from . import views
from django.conf.urls import url
from box.views import *
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required

from django.contrib import admin 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *


        
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.index,name='index'),
    path('chatbox',login_required(views.chatbox),name='chatbox'),
    path('log',views.log,name='log'),
    url(r'^search_user/$', views.search_user, name='search_user'),
    path('image_upload', image_upload, name = 'image_upload'),
   # path('success', success, name = 'success'),

    #      path('likepost',views.likepost, name='likepost'),
    url(r'^msg_to_database/$', views.msg_to_database, name='msg_to_database'),   # likepost view at /likepostsahi ????
    url(r'^fetch_data/$',views.fetch_data,name='fetch_data'),






    
 
    
 #   path('hotel_images', display_hotel_images, name = 'hotel_images'),

  ]

  
if settings.DEBUG: 
		urlpatterns += static(settings.MEDIA_URL, 
							document_root=settings.MEDIA_ROOT) 
  

