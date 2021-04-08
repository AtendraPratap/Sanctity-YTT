from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

# from dsa.models import *

class UserRegForm(UserCreationForm):
	email = forms.EmailField(max_length=100, help_text='Please enter a valid email address')
	

	class Meta(UserCreationForm):
		model = get_user_model()
		fields = ('email', 'password1', 'password2')

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = get_user_model().objects.get(email=email)
		except Exception as e:
			return email
		raise forms.ValidationError(f'Email {email} is already in use.')
		

class DsaAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label="Password", widget=forms.PasswordInput)

	class Meta:
		model  = get_user_model()
		fields = ("email", "password")

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError('Email or password is incorrect.')
		