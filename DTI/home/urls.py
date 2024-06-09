from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Signin',views.signin,name='signin'),
    path('Login',views.login,name='login'),
    path('Buddy',views.main_page,name='buddy'),
]