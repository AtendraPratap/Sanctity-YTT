from django.urls import path
from . import views
from website.views import *


urlpatterns = [
	path('dashboard/', views.dsa_dashboard, name='dashboard'),
    path('login/', views.dsa_login, name='dsalogin'),
    path('logout/', views.dsa_logout, name= 'logout'),
    path('signup/', views.dsa_Signup, name='dsasignup'),
    # path('activate/<uidb64>/<token>/',views.activate, name='activate'),
]
