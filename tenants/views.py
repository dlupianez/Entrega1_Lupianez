from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from tenants.models import Tenant

class TenantsListView(LoginRequiredMixin, ListView):
    model = Tenant
    template_name = 'tenants/tenants-list.html'

class TenantCreateView(LoginRequiredMixin, CreateView):
    model = Tenant
    template_name = 'tenants/tenant-create.html'
    fields = '__all__'
    success_url = '/tenants/tenants-list/'

class TenantUpdateView(UpdateView):
    model = Tenant
    template_name = 'tenants/tenant-update.html'
    fields = '__all__'
    success_url = '/tenants/tenants-list/'

class TenantDeleteView(DeleteView):
    model = Tenant
    template_name = 'tenants/tenant-delete.html'
    fields = '__all__'
    success_url = '/tenants/tenants-list/'