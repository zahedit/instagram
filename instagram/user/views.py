# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# from django.http import HttpResponse
from typing import Any, Dict, Optional
from django.db import models
from django.http import HttpResponse
from django.contrib.auth import login, get_user_model
from django.views.generic import FormView, UpdateView, DetailView
from user.forms import RegistrationForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from relation.models import Relation

User = get_user_model()

class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'user/register.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
#############################################
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return super().form_valid(form)
    # def form_valid(self, form):
    #     user = authenticate() #if user is exist everything is fine!
#############################################
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('username', 'avatar', 'bio', 'website')
    template_name = 'user/profile_update.html'
    success_url = '/'

    def get_object(self, queryset=None) :
        return self.request.user
#############################################
class ProfileDetailView(DetailView):
    model = User
    slug_url_kwarg = 'username' #variable that comes from url
    slug_field = 'username' #the word that comes from url equals to what name? exp: username = username
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs): #find the username, and pass it to template as object
        context = super(ProfileDetailView, self).get_context_data(**kwargs) #call the super of this function can use super() too
        user = self.get_object()
        context['posts_count'] = user.posts.count() #related_name = posts (for post model > user)
        context['followers_count'] = user.followers.count() # from Relation model get the [from_user] as related_name= followers
        context['followings_count'] = user.followings.count()
        context['is_following'] = Relation.objects.filter(from_user= self.request.user, to_user= user).exists() #if is true > they follow
        if self.request.user == user:
            context['is_the_same'] = True
        return context