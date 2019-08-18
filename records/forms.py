from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'age',
            'phone',
            'department',
        ]        