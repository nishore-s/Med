from django import forms
from .models import Medicine
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class MedicineForm(forms.ModelForm):
    class Meta:
        model=Medicine
        fields=["name","stock"]
class SignupForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
       model=User
       fields=["username","email","password1","password2"]
