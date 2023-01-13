from django.views.generic import ListView, CreateView
#from django.shortcuts import render

from tenants.models import Tenant
#from apartments.forms import ApartmentForm

class TenantsListView(ListView):
    model = Tenant
    template_name = 'tenants/tenants-list.html'

class TenantCreateView(CreateView):
    model = Tenant
    template_name = 'tenants/tenant-create.html'
    fields = '__all__'
    success_url = '/tenants/tenants-list/'