from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import*
from .models import*
from django.views.generic import TemplateView #A test view to be deleted
# Create your views here.


#Just a test view to be deleted later
class ModelView(TemplateView):
    template_name = "home.html"