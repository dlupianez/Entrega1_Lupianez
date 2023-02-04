from django.urls import path
from tenants.views import TenantsListView, TenantCreateView, TenantUpdateView, TenantDeleteView

urlpatterns = [
    path('tenants-list/', TenantsListView.as_view(), name='tenants_list'),
    path('tenant-create/', TenantCreateView.as_view(), name='tenant_create'),
    path('tenant-update/<int:pk>/', TenantUpdateView.as_view(), name='tenant_update'),
    path('tenant-delete/<int:pk>/', TenantDeleteView.as_view(), name='tenant_delete'),
]
