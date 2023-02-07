from django.contrib import admin
from rentals.models import Rent

# Register your models here.
@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('apartment','tenant','payday','total_paid','debt','receipt_of_payment','has_debt')
    list_filter = ("apartment", )
    search_fields = ("door_number__startswith", )
