from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    adress = models.CharField(max_length=255, default='adress')
    phone = models.CharField(max_length=255)