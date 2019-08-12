from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    college_name = models.CharField(max_length=100, blank=True, null=True, default='IIITDMJ',)