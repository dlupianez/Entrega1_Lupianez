from django.db import models

# Create your models here.

class Tenant(models.Model):
    """Definition of the Tenant class"""
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
