from django.contrib import admin
from apartments.models import Apartment

# Register your models here.
@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('door_number','rental_value','garage_value','expenses_value','total_value','is_available')
    list_filter = ("door_number", )
    search_fields = ("door_number__startswith", )