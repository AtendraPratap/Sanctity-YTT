from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils import timezone
# Create your models here.

class CustomUserManager(BaseUserManager):
   
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
    	user = self.create_user(
    		email = self.normalize_email(email),
    		password = password,
    	)
    	user.is_admin = True
    	user.is_staff = True
    	user.is_superuser = True
    	user.save(using=self._db)
    	return user


class CustomUser(AbstractBaseUser):

	email = models.EmailField(verbose_name='email address', unique=True)

	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_admin     = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login  = models.DateTimeField(verbose_name='last login', auto_now=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
	    return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_lable):
		return True