from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Donar,Patient


class Registerform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email',]
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email alrady registed')
        else:
            return email


class Donorform(forms.ModelForm):
    class Meta:
        model = Donar
        fields='__all__'
        exclude = ['user']
class Patiendform(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude=['user','donar','status']