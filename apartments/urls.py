from django.urls import path
from apartments.views import ApartmentsListView, ApartmentCreateView, list_apartments_search, ApartmentUpdateView, ApartmentDeleteView

urlpatterns = [
    path('apartments-list/', ApartmentsListView.as_view(), name='apartments_list'),
    path('apartment-create/', ApartmentCreateView.as_view(), name='apartment_create'),
    path('apartments-list-search/', list_apartments_search),
    path('apartment-update/<int:pk>/', ApartmentUpdateView.as_view(), name='apartment_update'),
    path('apartment-delete/<int:pk>/', ApartmentDeleteView.as_view(), name='apartment_delete'),
]