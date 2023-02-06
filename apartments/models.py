from django.db import models
import computed_property

# Create your models here.

class Apartment(models.Model):
    """Definition of the Apartment class"""
    door_number=models.CharField(max_length=10, null=False, blank=False)
    rental_value=models.FloatField()
    garage_value=models.FloatField()
    expenses_value=models.FloatField()
    total_value = computed_property.ComputedFloatField(compute_from='calculate_total_value') 
    is_available=models.BooleanField(default=True)
    apartment_picture = models.ImageField(upload_to='apartment_images', null=True, blank=True)

    def __str__(self):
        return self.door_number

    def calculate_total_value(self)-> float:
        return self.rental_value + self.garage_value + self.expenses_value