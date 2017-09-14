from django import forms
from .models import *
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    login = forms.CharField(label = 'Login')
    password = forms.CharField(widget = forms.PasswordInput, label = 'Hasło')

class OrderForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea, label=' Opis', required=False)
    quantity = forms.IntegerField(min_value=1, label='Ilość', initial=1)
