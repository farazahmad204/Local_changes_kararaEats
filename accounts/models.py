from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    whatsapp_num = models.CharField(max_length=15, blank=True, null=True, unique=True)
    address = models.CharField(max_length=250, blank=True, null=True,unique=False)
    # Email (inherited from AbstractUser, but can be customized)
    email = models.EmailField(unique=True)  # Ensure email is unique and required
