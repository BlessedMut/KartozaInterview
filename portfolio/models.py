from django.contrib.auth.models import AbstractUser
from django.db import models


# Extend User profile
class Profiles(AbstractUser):
    """
    The Profiles model extends the built-in django User model and appends the address, phone number fields as well
    as the location coordinates for users capturing their longitude and latitude points
    """
    address = models.TextField(blank=False, null=False)
    phone = models.CharField(blank=False, max_length=15, null=False)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
