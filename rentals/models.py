from django.db import models

# Create your models here.

class Rent(models.Model):
    """Definition of the Rent class"""
    payday=models.DateField()
    total_paid=models.FloatField()
    debt=models.FloatField()
    receipt_of_payent=models.IntegerField()