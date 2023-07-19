from typing import Any, Dict
from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        if User.objects.filter(username = self.cleaned_data['username']).exists():
            raise forms.ValidationError(_("Username already exists"))
        if User.objects.filter(email = self.cleaned_data['email']).exists():
            raise forms.ValidationError(_("Email address already exists"))
        return self.cleaned_data
    
    def save(self):
        user = User.objects.create_user(**self.cleaned_data) #create_user => hash the password
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user = User.objects.filter(username = self.cleaned_data['username']).first()
        if user is None:
            raise forms.ValidationError(_("Username doesn't exists"))
        
        # if not user.check_password(self.cleaned_data['password']):
        #     raise forms.ValidationError(_("Wrong password"))

        user = authenticate(**self.cleaned_data)
        if user is None:
            raise forms.ValidationError(_("Unable to login with provided credentials"))

        self.cleaned_data['user'] = user
        return self.cleaned_data