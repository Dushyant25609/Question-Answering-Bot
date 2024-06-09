from django import forms
from .models import Signin

class SignupForm(forms.ModelForm):
    class Meta:
        model = Signin
        fields = ['name','phone','email','password']