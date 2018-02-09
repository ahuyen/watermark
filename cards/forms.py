from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First name', max_length=256)
    last_name = forms.CharField(label='Last name', max_length=256)
    pass