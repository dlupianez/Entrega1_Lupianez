from django.urls import path
from tenants.views import TenantsListView, TenantCreateView

urlpatterns = [
    path('tenants-list/', TenantsListView.as_view(), name='tenants_list'),
    path('tenant-create/', TenantCreateView.as_view(), name='tenant_create'),
]