from django.db import models
from django.utils import timezone
from django.contrib import admin
# from .validators import validate_file

class Basic_Details(models.Model):
    #Basic details component

    GENDER_CHOICES = [
    ("Male", ("Male")),
    ("Female", ("Female")),
    ("Other", ("Other"))
    ]
    
    #basic info
    entry_date = models.DateField(default=timezone.now)
    created_time = models.TimeField(default=timezone.now)
    # account holder info 

    first_name = models.CharField(max_length=100,null = True)
    last_name = models.CharField(max_length=100,null = True)
    gender = models.CharField(max_length=10,null = True,choices=GENDER_CHOICES, blank=False)
    father_name = models.CharField(max_length= 100, null=True)
    mother_name = models.CharField(max_length= 100, null=True , blank =True)
    date_of_birth = models.DateField(blank=True,null = True)

    # account holder address info
    current_address = models.TextField(null=True )
    
    city = models.CharField(max_length= 100, null=True  )
    district = models.CharField(max_length= 100, null=True  )
    state = models.CharField(max_length= 100, null=True  )
    pincode = models.CharField(max_length= 100, null=True  )
    country = models.CharField(max_length= 100, null=True)
      
    email_id = models.EmailField(max_length = 100 , null =True, blank = True)
    permanent_address = models.TextField(null=True )
    mobile_number_1 = models.CharField(max_length = 10, null=True )
    mobile_number_2 = models.CharField(max_length = 10, null=True, blank =True)

    # id proof component
    pan = models.CharField(max_length=200, null=True, blank=True)
    aadhar = models.CharField(max_length=200, null=True, blank=True)
    pan_image = models.FileField(upload_to='pan/', null=True, blank=True)
    aadhar_front = models.FileField(upload_to='aadhar_f/', null=True, blank=True)
    aadhar_back = models.FileField(upload_to='aadhar_b/', null=True, blank=True)
    user_image = models.ImageField(upload_to='user_image/', null=True, blank=False)

    # extra fields for DSA form
    dsa_experience = models.IntegerField(null=True, blank=True)
    business_name  = models.CharField(max_length=200, null=True, blank=False)
    pan_or_aadhar  = models.FileField(null=True, blank=False, upload_to='dsa_docs/')


    

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title() 
        self.last_name = self.last_name.title() if(self.last_name) else self.last_name
        self.father_name = self.father_name.title() if(self.father_name) else self.father_name
        self.mother_name = self.mother_name.title() if(self.mother_name) else self.mother_name
        self.current_address = self.current_address.title() if(self.current_address) else self.current_address 
        self.permanent_address = self.permanent_address.title() if(self.permanent_address) else self.permanent_address
        super(Basic_Details, self).save(*args, **kwargs)


class Bank_Details(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    account_number = models.CharField(max_length=200, null=True, blank=False)
    IFSC_CODE = models.CharField(max_length=200, null=True, blank=False)

class PL_Docs(models.Model):
    salary_slip = models.FileField(upload_to='PL/salary_slip/', null=True, blank=True)
    bank_statement = models.FileField(upload_to='PL/bank_statement/', null=True, blank=True)
    residential_proof = models.FileField(upload_to='PL/res_proof/', null=True, blank=True)

class PL_reference(models.Model):
    RELATIONSHIP_CHOICES = [
        ("Father", ("Father")),
        ("Mother", ("Mother")),
        ("Brother", ("Brother")),
        ("Sister", ("Sister")),
    ]
    ref_1_name = models.CharField(max_length=200, null=True, blank=False)
    ref_2_name = models.CharField(max_length=200, null=True, blank=False)
    ref_1_contact = models.CharField(max_length=200, null=True, blank=False)
    ref_2_contact = models.CharField(max_length=200, null=True, blank=False)
    ref_1_relationship = models.CharField(max_length=200, null=True, blank=False)
    ref_2_relationship = models.CharField(max_length=200, null=True, blank=False)

class PL(Basic_Details):
    PROPERTY_CHOICES = [
    ("Rented", ("Rented")),
    ("Leased", ("Leased")),
    ("Self", ("Self")),
    ("Other", ("Other"))
    ]
    EMPLOYMENT_CHOICES = [
    ("Salaried", ("Salaried")),
    ("Self-Employed", ("Self-Employed")),
    ("Self", ("Self")),
    ("Other", ("Other"))
    ]
    EDUCATION_CHOICES = [
    ("10th", ("10th")),
    ("10+2", ("10+2")),
    ("Graduate", ("Graduate")),
    ("Post-Graduate", ("Post-Graduate"))
    ]
    newsletter = models.BooleanField(default=True, null=False)
    education = models.CharField(max_length=20,null = True,choices=EDUCATION_CHOICES,  blank=False )
    married = models.BooleanField(default=False)
    property_ownership_status = models.CharField(max_length=20,null = True, choices=PROPERTY_CHOICES,  blank=False)
    no_of_years_at_residence = models.IntegerField(null=True, blank=True)
    employment_type = models.CharField(max_length=15,null = True,choices=EMPLOYMENT_CHOICES,  blank=False)
    bank_details = models.ForeignKey(Bank_Details, on_delete=models.CASCADE, null=True)
    docs = models.ForeignKey(PL_Docs, on_delete=models.CASCADE, null=True)
    references = models.ForeignKey(PL_reference, on_delete=models.CASCADE, null=True)

        

class Contact(models.Model):
    #basic info
    created_time = models.DateField(default=timezone.now)
    name = models.CharField(max_length=200,null = True,blank=True)
    email = models.CharField(max_length=200,null = True,blank=True)
    phone = models.CharField(max_length=200,null = True,blank=True)
    message = models.TextField(null=True, blank=True)


class Business_Loan(models. Model):
    firstName       =    models.CharField(max_length=30, null=True, blank=True)
    lastName        =    models.CharField(max_length=30, null=True, blank=True)
    contactNum      =    models.CharField(max_length=13, null=True, blank=True)
