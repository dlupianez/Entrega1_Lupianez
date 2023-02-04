from django.urls import path
from tenants.views import TenantsListView, TenantCreateView, TenantUpdateView

urlpatterns = [
    path('tenants-list/', TenantsListView.as_view(), name='tenants_list'),
    path('tenant-create/', TenantCreateView.as_view(), name='tenant_create'),
    path('tenant-update/<int:pk>/', TenantUpdateView.as_view(), name='tenant_update'),
]
