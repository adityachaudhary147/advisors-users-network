from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,BaseUserManager



class User(AbstractUser):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    username=models.CharField(max_length=255,unique=False,default="username")
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
