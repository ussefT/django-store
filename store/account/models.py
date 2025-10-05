from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# Create your models here.

# change user info
class User(AbstractUser):
    email=models.EmailField("Email Address")
    phone=models.CharField("Phone Number",max_length=15)
    address=models.TextField("Address")
    avatar=models.ImageField(upload_to='avatars/')

    def __str__(self):
        return f"{self.username}"