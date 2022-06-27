from asyncio.format_helpers import extract_stack
from pyexpat import model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""


    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False, **extra_fields):
       
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user = self.model(
            email=self.normalize_email(email), 
            **extra_fields
        )
        
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password,  **extra_fields):
        user = self.create_user(
            email=email,
            password=password,
            is_admin=True,
            is_staff=True, 
            **extra_fields
            
        )
        return user




class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

   
    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active 
    
    def has_perm(self, perm, obj=None):
        return self.staff

    def has_module_perms(self, app_label):
        return self.staff