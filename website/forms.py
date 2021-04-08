from dsa.models import *
from website.models import *
from django import forms
import os


class DateInput(forms.DateInput):
    input_type = 'date'


class DSAForm(forms.ModelForm):    
    class Meta:
        model = DSA
        fields = ('first_name', 'last_name', 'email_id', 'mobile_number_1', 'city', 'dsa_experience', 'business_name', 'pan_or_aadhar',)


        # def clean_email(self):

        # # Get the email
        #     email = self.cleaned_data.get('email')

        # # Check to see if any users already exist with this email as a username.
        #     try:
        #         match = User.objects.get(email=email)
        #     except User.DoesNotExist:

        #     # Unable to find a user, this is fine
        #         return email

        # # A user was found with this as a username, raise an error.
        #     raise forms.ValidationError( "This email address is already in use. Please supply a different email address.")



class PLHomePageForm(forms.ModelForm):
    class Meta:
        model = PL
        fields = ('first_name', 'last_name', 'mobile_number_1', 'email_id',)


class PLForm(forms.ModelForm):    
    class Meta:
        model = PL
        fields = ('first_name', 'last_name', 'email_id', 'mobile_number_1', 'newsletter',)
       

class ContactForm(forms.ModelForm):    
    class Meta:
        model = Contact
        exclude = ('created_time',)
