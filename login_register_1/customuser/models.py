from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self,email,name,password):
        if not email:
            raise ValueError("Enter email")

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,name,password):
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user




class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=200,unique=True)
    name=models.CharField(max_length=100)
    is_active = models.BigIntegerField(default=True)
    is_staff = models.BigIntegerField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
