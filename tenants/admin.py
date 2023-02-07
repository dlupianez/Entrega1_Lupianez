from django.contrib import admin
from tenants.models import Tenant

# Register your models here.
@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name','lastname','email','phone','is_active')
    search_fields = ("lastname__startswith", )
