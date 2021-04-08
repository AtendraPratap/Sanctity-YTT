from django.shortcuts import render, redirect
from website.forms import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from post_office import mail
from .models import *
from django.contrib import messages
import requests
import json
import urllib


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PLHomePageForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['phone_new_application'] = form.cleaned_data['mobile_number_1']
            return redirect('personal-loan')
        else:
            print(form.errors)
    else:
        form = PLHomePageForm()

    context = {'form': form}
    return render(request, 'website/index.html', context)

def personalloan(request):
    context = {}
    if request.method == 'POST':
        form = PLForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'website/form_success/personal_loan.html')
        else:
            print(form.errors)

    else:
        if 'phone_new_application' in request.session:
            instance = PL.objects.all(mobile_number_1=request.session['phone_new_application']).first()
            form = PLForm(instance=instance)
        else:
            form = PLForm()
    context['form'] = form
    return render(request, 'website/personal-loan.html', context)

def about(request):

    return render(request, 'website/about.html')

def dsa(request):
    if request.method == 'POST':
        form = DSAForm(request.POST, request.FILES)
        if form.is_valid():
            print('hey you!')
            print(form.errors)
            form.save()
            return redirect('dsasignup')
        else:
            messages.error(request, 'Please fill the form correctly')
            return render(request, 'dsa/dsa.html')


    else:
        form = DSAForm()
    
    context = {'form': form}
    return render(request, 'dsa/dsa.html', context)

def get_otp(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        mobile = f'+91{mobile}'
        url = f'http://smpp.valueleaf.com/generateOtp.jsp?userid=MoneyOTP&key=4c0d6ef033XX&mobileno={mobile}&timetoalive=60'
        otp = requests.get(url)
        if 'success' in otp.text:
            return HttpResponse('SUCCESS', status=200)
        else:
            return HttpResponse('Wrong', status=422)


def verify_otp(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        number = f'+91{number}'
        otp = request.POST.get('otp')
        url = f'http://smpp.valueleaf.com/validateOtpApi.jsp?mobileno={number}&otp={otp}'
        sotp = requests.get(url)
        print(sotp.text)
        if 'success' in sotp.text:
            return HttpResponse('success', content_type='text/plain')
        else:
            return HttpResponse('wrong', content_type='text/plain')

    return HttpResponse(status=200)


def loan_sms(request):
    if request.method == 'POST':
        form = PLForm(request.POST)
        mobile = request.POST.get('mobile')
        mobile = f'+91{mobile}'
        print(mobile)

        url = f'http://smpp.valueleaf.com/sendsms.jsp?user=MoneyOTP&password=4c0d6ef033XX&senderid=SMSNOW&mobiles={mobile}&sms=Thanks for applying at Moneyply. Please click on the following link for further process. Link: https://smarturl.it/CASHe_Moneyply'
        sms = requests.get(url)
        if 'success' in sms.text:
            return HttpResponse('SUCCESS', status=200)
        else:
            return HttpResponse('WRONG', status=422)

    

def privacy(request):

    return render(request, 'website/privacy.html')

def tnc(request):

    return render(request, 'website/tnc.html')

def blogs(request):

    return render(request, 'website/blogs.html')

def blog_single(request):

    return render(request, 'website/blog-single.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            mail_subject = 'New Query on MoneyPly.in'
            message = render_to_string('website/email/contact.html', {
                'name': form.cleaned_data['name'],
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            })
            to_email = ['shreyansh@moneyply.in']
            mail.send(
                to_email,
                subject = mail_subject,
                sender = settings.EMAIL_HOST_USER,
                message = message,
            )
            return HttpResponse('Contact Success')
        else:
            print(form.errors)
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'website/contact.html', context)

def custom_page_not_found_view(request, exception):
    return render(request, "website/errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "website/errors/500.html", {})

# def custom_permission_denied_view(request, exception=None):
#     return render(request, "errors/403.html", {})

# def custom_bad_request_view(request, exception=None):
#     return render(request, "errors/400.html", {})


# Following views are for business loan

def businessLoan(request):
    return render(request, 'website/bl.html')