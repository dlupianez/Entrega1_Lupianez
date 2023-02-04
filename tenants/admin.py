from django.contrib import admin
from tenants.models import Tenant

# Register your models here.
@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('lastname',)
