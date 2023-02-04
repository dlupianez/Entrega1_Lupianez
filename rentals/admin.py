from django.contrib import admin
from rentals.models import Rent

# Register your models here.
@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('payday',)

