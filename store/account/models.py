from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# Create your models here.

from django.utils import timezone
import uuid
import os
def _get_avatar_upload_path(obj,filename):
    """object model , filename name image upload"""
    now=timezone.now()
    base_path="avatars"
    new_filename=str(uuid.uuid5(uuid.NAMESPACE_URL,obj.pk))
    ext=os.path.splitext(filename)[1]
    p=os.path.join(base_path,now.strftime("%Y/%m/%d"),f"{new_filename}{ext}")
    return p


# change user info
class User(AbstractUser):
    email=models.EmailField("Email Address")
    phone=models.CharField("Phone Number",max_length=15)
    address=models.TextField("Address",blank=True,null=True)
    # use callback function
    avatar=models.ImageField(upload_to=_get_avatar_upload_path,blank=True,null=True)

    def __str__(self):
        return f"{self.username}"