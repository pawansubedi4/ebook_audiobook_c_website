from django import forms
from .models import Ebook,audiobook
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EbookForm(forms.ModelForm):
    class Meta:
        model = Ebook
        fields = ['name', 'image', 'price','detail','category','author','pdf',]

class Createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2',]

class AudiobookForm(forms.ModelForm):
    class Meta:
        model = audiobook
        fields = ['name', 'image', 'price','detail','category','author','audio',]