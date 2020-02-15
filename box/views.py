from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView
from .forms import *
from .models import *
from django.core.serializers import serialize
from django.contrib.auth.models import User


def Searchform(request):
    if request.method=='GET':
        subject_id=request.GET['username']

        m = User(username=subject_id) # Creating Like Object
        ipdb.set_trace()
        #model =globals()[subject_id]
        searchpost=m.objects.filter(username=subject_id)
        searchpost=serialize('json', searchpost) 
        return HttpResponse(searchpost)
    else:
        return HttpResponse("not success")

# Create your views here.

def index(request):
    return render(request,'index.html')

def topics(request):
    return render(request,'registration/topic.html')

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