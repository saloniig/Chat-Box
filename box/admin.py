from django.contrib import admin

# Register your models here.
from .models import user,detail,message

admin.site.register(user)
admin.site.register(detail)
admin.site.register(message)
