from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget = forms.TextInput(attrs={
        "class": "form__input",
        'placeholder': 'username'
    }))
    email = forms.EmailField(max_length=200, help_text='required', widget = forms.TextInput(attrs={
        "class": "form__input",
        'placeholder' : 'Email'
    }))
    password1 = forms.CharField(max_length=200, help_text='required', widget = forms.PasswordInput(attrs={
        "class": "form__input",
        'placeholder' : 'Password'
    }))
    password2 = forms.CharField(max_length=200, help_text='required', widget = forms.PasswordInput(attrs={
        "class": "form__input",
        'placeholder' : 'Confirm Password'
    }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={"class": "form__input",'placeholder': 'username'}),
            'email': forms.TextInput(attrs={"class": "form__input",'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={"class": "form__input",'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={"class": "form__input",'placeholder': 'Confirm Password'}),
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.Form):
    start_date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date',
        "class": "form__input",
        }), required=True, )
    end_date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date',
        "class": "form__input",
        }), required=True)
