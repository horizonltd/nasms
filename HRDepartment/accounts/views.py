from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from . import forms
from django.views.generic import CreateView

# Create your views here.

class SignUp(CreateView):

    form_class = forms.UserCreateForm

    #When user create account successful, redirect him to login
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
