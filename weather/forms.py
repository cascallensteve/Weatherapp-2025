from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput, PasswordInput, NumberInput
from .models import User

from django.contrib.auth.models import User


class Register(forms.ModelForm):

    class Meta:
        model = User  # Using Django's built-in User model
        fields = ['username', 'email', 'password_1', 'password_2']

# username=forms.TextInput(
#     widget=forms.Textinput(attr={
#         'class': 'form-control', 
#             'placeholder': 'Enter Your Phone Number',
#             'required': True
#     })
# )

    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter your Email',
            'required': True
        })
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter Your Phone Number',
            'required': True
        })
    )

    password_1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password',
            'required': True
        })
    )


    password_2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password',
            'required': True
        })
    )

   