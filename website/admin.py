from django.contrib import admin
from dsa.models import *
from website.models import *
# Register your models here.


@admin.register(PL)

class PLAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'mobile_number_1', 'email_id', 'city')


@admin.register(DSA)

class DSAAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'business_name', 'email_id')

