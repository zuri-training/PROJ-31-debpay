from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ContendForm, HelpForm, DebtorForm, PostForm
from .models import*

#Just a test view to be deleted later
def contend_view(request):
    context = {}

    form = ContendForm(request.POST)

    #To check if form is valid
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "home.html", context)

def help_view(request):
    context = {}

    form = HelpForm(request.POST)

    #To check if form is valid
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "help_page.html", context)

def debtor_form_view(request):
    context = {}

    form = DebtorForm(request.POST)

    #To check if form is valid
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "debtor_form.html", context)