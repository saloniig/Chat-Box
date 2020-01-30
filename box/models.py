from django.db import models

# Create your models here.
class user(models.Model):
    id=models.AutoField(primary_key=True,blank=True,null=False)
    email=models.EmailField(max_length = 254,blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    def __str__(self):
        return str(self.id)  
    
class detail(models.Model):
    id = models.OneToOneField(
        user,
        on_delete=models.CASCADE,
        primary_key=True,
        blank=True,
        null=False
    )
    username=models.CharField(max_length=100,blank=True,null=True)
    name=models.CharField(max_length=100,blank=True,null=True) 
    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return self.username

class message(models.Model):
    group_id=models.AutoField(primary_key=True,blank=True, null=False)
    recipient_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=False)
    username=models.ForeignKey(detail,on_delete=models.CASCADE,blank=True,null=False)
    
    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    def __str__(self):
        return str(self.group_id)
    