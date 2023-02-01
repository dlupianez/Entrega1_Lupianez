from django.db import models

# Create your models here.

class Tenant(models.Model):
    """Definition of the Tenant class"""
    name=models.CharField(max_length=50, null=False, blank=False)
    lastname=models.CharField(max_length=50, null=False, blank=False )
    email=models.EmailField(max_length=50, null=False, blank=False)
    phone=models.CharField(max_length=50, null=False, blank=False)
    is_active=models.BooleanField(default=True)
    tenant_picture = models.ImageField(upload_to='tenant_images', null=True, blank=True)

    def __str__(self):
        return self.lastname