# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# from django.http import HttpResponse
from django.http import HttpResponse
from django.contrib.auth import login
from django.views.generic import FormView
from user.forms import RegistrationForm, LoginForm

class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'user/register.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return super().form_valid(form)
    # def form_valid(self, form):
    #     user = authenticate() #if user is exist everything is fine!