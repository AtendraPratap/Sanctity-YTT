from django.db import models
from .models import *
from website.models import *
# Create your models here.
class DSA(Basic_Details):
    education = models.CharField(max_length=200, null=True, blank=True)
    referral_id = models.CharField(max_length=15, null=True, blank=True)
    referred_by = models.CharField(max_length=15, null=True, blank=True)
    approved = models.BooleanField(default=False, null=False)