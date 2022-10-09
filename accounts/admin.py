from django.contrib import admin
from .models import Profile, UserPhoneNumber, UserAddress

# Register your models here.

admin.site.register(Profile)
admin.site.register(UserAddress)
admin.site.register(UserPhoneNumber)
