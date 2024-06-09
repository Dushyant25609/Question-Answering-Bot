from django.contrib import admin
from .models import Signin
# Register your models here.

class SigninAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'password')


admin.site.register(Signin, SigninAdmin)