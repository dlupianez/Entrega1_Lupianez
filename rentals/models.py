from django.db import models
from apartments.models import Apartment
from tenants.models import Tenant


# Create your models here.

class Rent(models.Model):
    """Definition of the Rent class"""
    apartment = models.ForeignKey(Apartment, blank=False, null=False, on_delete=models.CASCADE, related_name='apartment')
    tenant = models.ForeignKey(Tenant, blank=False, null=False, on_delete=models.CASCADE, related_name='tenant')
    payday=models.DateField()
    total_paid=models.FloatField()
    debt=models.FloatField()
    receipt_of_payment=models.IntegerField()
    has_debt=models.BooleanField(default=False)    