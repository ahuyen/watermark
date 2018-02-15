from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.validators import validate_email

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First name', max_length=256)
    last_name = forms.CharField(label='Last name', max_length=256)
    email = forms.CharField(label='Email', max_length=256)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        validate_email(email)        

class LoginForm(AuthenticationForm):
    pass
