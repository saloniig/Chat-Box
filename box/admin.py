from django.contrib import admin

# Register your models here.
from .models import topic,message

admin.site.register(topic)
admin.site.register(message)