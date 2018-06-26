from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import FormView

class Signupform(forms.Form):
    user_name = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email  = forms.EmailField()

class Signinform(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget= forms.PasswordInput)



class Resetform(forms.Form):
    email = forms.EmailField()

class UserDetail(forms.Form):
    DIERCTION = (('1','EAST'),('2','WEST'),('3','NORTH'),('4','SOUTH'))
    user_name = forms.CharField(required=True,max_length=30)
    location = forms.CharField(required=True,max_length=30)
    Kison_No = forms.DecimalField
    direction = forms.ChoiceField(widget=forms.Select,choices=DIERCTION)



