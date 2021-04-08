from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('personal-loan/', views.personalloan, name='personal-loan'),
    path('dsa/', views.dsa, name='dsa'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('terms-conditions/', views.tnc, name='tnc'),
    # path('blogs/', views.blogs, name='blog_main'),
    # path('blogs/blog-single/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
    path('otp/', views.get_otp, name='otp'),
    path('votp/', views.verify_otp, name='verify_otp'),
    path('sms_confirm/', views.loan_sms, name='loan-sms'),
    path("sitemap.xml/", TemplateView.as_view(template_name="website/sitemap.xml", content_type="text/plain")),
    path('robots.txt/', TemplateView.as_view(template_name="website/robots.txt", content_type="text/plain")),

    # Business loan urls

    path('business-loan/', views.businessLoan, name='business_loan')
]