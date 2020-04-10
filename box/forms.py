from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from box.models import *

# forms.py 


class HotelForm(forms.ModelForm): 

	class Meta: 
		model = Hotel 
		fields = ['person_id','hotel_Main_Img'] 


