from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView
from .forms import *
from .models import *
from django.core.serializers import serialize
from django.contrib.auth.models import User
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Max
import ipdb
from django.contrib.auth.models import User
import os
from django.urls import reverse_lazy




def fetch_data(request):
    query=message.objects.filter(receiver_id = request.user.id, sender_id= request.GET.get("reciever_id")).order_by("-created_on")
    context={
            'message':query.values_list()[0][3],
            'datetime':str(query.values_list()[0][4]),
            'datetim':str(query.values_list()[1][4]),

           }
    #ipdb.set_trace()
    context = json.dumps(context, sort_keys = True)
    return HttpResponse(context)


def hotel_image_view(request):

    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        image_name = "images/" + str(request.FILES['file'])

        user_objects = User.objects.get(id = request.user.id) 
        image = Hotel.objects.create(hotel_Main_Img=image_name,person_id=user_objects)
      

        image.save()
        #ipdb.set_trace() 
        return redirect('/topic')

    else:

        subject_objects = User.objects.all()
        return render(request,'registration/hotel_image_form.html', {'name':request.user.username, 'subject_objects' : subject_objects})
    return HttpResponse("Failed")


def handle_uploaded_file(file, filename):
    if not os.path.exists('media/images'):
        os.mkdir('media/images')
        
    with open('media/images/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
        return chunk

def likePost(request):
        if request.method == 'GET':
            if request.GET.get('post_id'):
                message_save=message.objects.create(content = request.GET.get('post_id'), sender_id = User.objects.get(id=request.user.id), receiver_id= User.objects.get(id= request.GET.get("reciever_id")))
                #ipdb.set_trace()

                message_save.save()
                #ipdb.set_trace()
                data={
                        "success_data": "done"
                }
                
                searchpost = json.dumps(data, sort_keys = True)
                #ipdb.set_trace()
                return HttpResponse(searchpost)

        else:
                return HttpResponse("Request method is not a GET")

def topics(request):
    if request.method == 'GET':



        user_objects = User.objects.get(username = request.user.username)
        Hotels = Hotel.objects.filter(person_id = user_objects.pk).order_by("-id")
        #ipdb.set_trace()
    return render(request,'registration/topic.html',{'hotel_images' : Hotels,'name':request.user.username,'users': User.objects.exclude(username=request.user.username)})

#def success(request):
    #print("Success")
    #return HttpResponse('successfully uploaded')
    #return render(request,'registration/topic.html')
def Searchform(request):
    if request.method=='GET':
        subject_id=request.GET['username']

        if(request.GET['username']!=request.user.username):
            searchpost=User.objects.get(username=subject_id)
            Hotels = Hotel.objects.filter(person_id = searchpost.pk).order_by("-id")
            if(Hotels.count()==0):
                hotel_Main_Img = "https://www.htmlcsscolor.com/preview/gallery/2C3E50.png"

               # hotel_Main_Img=Hotels.values_list()[0][2]
            else:
                hotel_Main_Img=Hotels.values_list()[0][2]

              #  hotel_Main_Img = "https://www.htmlcsscolor.com/preview/gallery/2C3E50.png" 
#            hotel_Main_Img=Hotels.values_list()[0][2]
       
            data={
                'username':searchpost.username,
                'first_name':searchpost.first_name,
                'last_name':searchpost.last_name,
                'email':searchpost.email,
                "id": searchpost.id,
                'hotel_Main_Img':hotel_Main_Img

            }

            sender_msg = message.objects.filter(receiver_id = request.user.id, sender_id= data["id"]).order_by("created_on").values_list('id', 'content', "sender_id")
            receiver_msg = message.objects.filter(sender_id = request.user.id, receiver_id= data["id"]).order_by("created_on").values_list('id', 'content', "sender_id")
            msg=list(sender_msg)+list(receiver_msg)
            msg = sorted(msg, key=lambda x: x[0])
            msg = dict(enumerate(msg))
            data.update({"msg" : msg}, sort_keys = True)
            searchpost = json.dumps(data, sort_keys = True)
            return HttpResponse(searchpost,{'hotel_images' : Hotels})
        else:
            return HttpResponse("bye")
    else:
        return HttpResponse("not success")

           

def index(request):

    return render(request,'index.html')


def log(request):
    return render(request,'registration/log.html')

                                   
