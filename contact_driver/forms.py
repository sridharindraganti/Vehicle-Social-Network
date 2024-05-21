from django import forms
from .models import Registration
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

class SearchForm(forms.Form):
    license_plate_number = forms.CharField(label='License Plate Number', max_length=20)
