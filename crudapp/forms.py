# from django.core import validators
from .models import student, User
from django import forms

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name','email','mobile','password']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "mobile": forms.NumberInput(attrs={'class': 'form-control'}),
            "password": forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        }

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username123', 'password123']
        widgets = {
            "username123": forms.TextInput(attrs={'class': 'form-control'}),
            "password123": forms.PasswordInput(attrs={'class': 'form-control'}),
        }