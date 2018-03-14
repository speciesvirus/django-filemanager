from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True, null=True, blank=True)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    country = models.IntegerField(null=True, blank=True)
    contact_person = models.CharField(max_length=150, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    office_phone_country = models.IntegerField(null=True, blank=True)
    office_phone = models.CharField(max_length=15, null=True, blank=True)
    mobile_phone_country = models.IntegerField(null=True, blank=True)
    mobile_phone = models.CharField(max_length=15, null=True, blank=True)
    tex_id = models.CharField(max_length=13, null=True, blank=True)
    avatar = models.CharField(max_length=3000, null=True, blank=False)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []