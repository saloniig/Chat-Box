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
  

      
def hotel_image_view(request): 

    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 

        #temp = request.POST['person_id']
  
        if form.is_valid():
           # user_objects = User.objects.all()
            #ipdb.set_trace() 
            post = form.save() 
            #post.person_id_id = 
            post.save()
            return redirect('success') 
    else: 
        form = HotelForm() 
        subject_objects = User.objects.all()
        return render(request, 'registration/hotel_image_form.html', {'form' : form, 'name':request.user.username, 'subject_objects' : subject_objects})


       # return render(request, 'registration/hotel_image_form.html', {'form' : form, 'name':request.user.username}) 
def topics(request):
    if request.method == 'GET':

#        person=request.GET('person_id')
#        model=request.GET('hotel_Main_Img')
#        search=model.objects.filter(person=person_id)    #hai tu ??haa you here? :)
                # getting all the objects of hotel.

        user_objects = User.objects.get(username = request.user.username)
        Hotels = Hotel.objects.filter(person_id = user_objects.pk).order_by("-id")
        #ipdb.set_trace()
    return render(request,'registration/topic.html',{'hotel_images' : Hotels,'name':request.user.username})



def success(request): 
    return HttpResponse('successfully uploaded') 

def Searchform(request):
    if request.method=='GET':
        subject_id=request.GET['username']

        #m = User(username=subject_id) 
        #model =globals()[subject_id]
        searchpost=User.objects.get(username=subject_id)
        #ipdb.set_trace()
        data={
            'username':searchpost.username,
            'first_name':searchpost.first_name,
            'last_name':searchpost.last_name,
            'email':searchpost.email
        }
        #searchpost=serialize('json', data) 
        searchpost = json.dumps(data, sort_keys = True)
        return HttpResponse(searchpost)
    else:
        return HttpResponse("not success")


 
def index(request):
    return render(request,'index.html')



def log(request):
    return render(request,'registration/log.html')

"""
    class emailform(FormView):
    def get(self,request):
    
        return render(request,'registration/email.html')
    def post(self, request):

       
        return render(request, 'registration/otp.html',{"sign_objects":sign_objects})
        
class otp(FormView):
    def get(self,request):
        return render(request,'registration/email.html')
    
    def post(self,request):
        form= emailForm(request.POST)     
        temp = request.POST['email']
        form.save()
        sign_objects = user.objects.all()
        return render(request, 'registration/otp.html',{"sign_objects":sign_objects,"temp":temp})
    



class signform(FormView):
    def get(self,request):
        return render(request,'registration/email.html')


    def post(self,request):
        form= signForm(request.POST)     
        form.save(commit=False)        


        return render(request,'registration/sign.html')

class AboutView(FormView):
    def get(self, request):
        return render(request, 'qw.html')

    def post(self, request):
        #form= signupForm(request.POST)     
        #form.save(commit=False)
        form= signForm(request.POST)     
        form.save(commit=False)        

        
     
        return render(request, 'qw.html')
"""