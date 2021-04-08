from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages
from django.urls import reverse
from dsa.forms import *
from django.contrib.auth.forms import AuthenticationForm
from website.forms import *
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import *
from . forms import UserRegForm, DsaAuthenticationForm

from django.conf import settings

User = get_user_model()

def dsa_Signup(request):

    user = request.user
    if user.is_authenticated:
        return HttpResponse(f'You are already authenticated as {user.email}.')

    context = {}
    if request.method == 'POST':
        form       = UserRegForm(request.POST)

        if form.is_valid():
            form.save()
            email         = form.cleaned_data.get('email')
            raw_password  = form.cleaned_data.get('password1')
            user      = authenticate(email=email, password=raw_password)
            login(request,user)
            return redirect('dsalogin')
        else:
            context['form'] = form

    else:
        form = DSAForm()
        context['form'] = form
    return render(request, 'dsa/signup.html', context)


def dsa_login(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = DsaAuthenticationForm(request.POST)
        if form.is_valid():
            email    = request.POST['email']
            password = request.POST['password']

            user = authenticate(email=email, password=password)
            print('dkafhd')

            if user is not None:
                login(request, user)
                messages.info(request, f'You are logged in as {email}')
                return redirect('dashboard')
            else:
                messages.error(request, 'Username or password is incorrect')

        else:
            print(form.errors)
            context['form'] = form
    else:
        # print('nice')
        form = DsaAuthenticationForm()
        context['form'] = form
    return render(request, 'dsa/login.html', context)


def dsa_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("dsalogin")


@login_required
def dsa_dashboard(request):
    return render(request, 'dsa/dashboard.html')