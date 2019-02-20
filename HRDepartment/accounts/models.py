from django.db import models
from django.contrib import auth
from django.forms import forms
from django.forms import TextInput, Textarea
# Create your models here.

#This is a predefined django function, for user login and authentication
class User(auth.models.User, auth.models.PermissionsMixin):

    #Automically set the a form for the user make it to DB
    def __str__(self):
        return "@{}".format(self.username)

