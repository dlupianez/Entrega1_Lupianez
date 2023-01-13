from django.db import models

# Create your models here.

class Apartment(models.Model):
    """Definition of the Apartment class"""
    door_number=models.CharField(max_length=10)
    rental_value=models.FloatField()
    garage_value=models.FloatField()
    expenses_value=models.FloatField()
    total_value=models.FloatField()