from django.db import models

# Create your models here.

class Apartment(models.Model):
    """Definition of the Apartment class"""
    door_number=models.CharField(max_length=10, null=False, blank=False)
    rental_value=models.FloatField()
    garage_value=models.FloatField()
    expenses_value=models.FloatField()
    total_value=models.FloatField()
    is_available=models.BooleanField(default=True)
    apartment_picture = models.ImageField(upload_to='apartment_images', null=True, blank=True)

    def __str__(self):
        return self.door_number