from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView

# Create your views here.
class AboutView(FormView):
    def get(self, request):
        return render(request, 'box/qw.html')

    def post(self, request):
        return render(request, 'box/qw.html')

class email(FormView):
    def get(self,request):
        return render(request,'box/email.html')


class otp(FormView):
    def get(self,request):
        return render(request,'box/email.html')
    
    def post(self,request):
        return render(request,'box/otp.html')



class signup(FormView):
    def get(self,request):
        return render(request,'box/email.html')


    def post(self,request):
        return render(request,'box/sign.html')