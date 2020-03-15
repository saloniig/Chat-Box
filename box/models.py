from django.db import models
from django.contrib.auth.models import User


class topic(models.Model):
    id=models.AutoField(primary_key=True,blank=True,null=False)
    creator_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=False,related_name='creator')
    receiver_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=False,related_name='receiver')
    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)    



class message(models.Model):
    id=models.AutoField(primary_key=True,blank=True,null=False)
    sender_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=False)
    topic_id=models.ForeignKey(topic,on_delete=models.CASCADE,blank=True,null=False)
    content=models.TextField(blank=True,null=False)
    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)    

class Hotel(models.Model): 
    person_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=False)
    hotel_Main_Img = models.ImageField(upload_to='images/') 

# Create your models here.
