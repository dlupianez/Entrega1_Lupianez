from django.urls import path
from rentals.views import RentalsListView, RentCreateView, RentUpdateView, RentDeleteView

urlpatterns = [
    path('rentals-list/', RentalsListView.as_view(), name='rentals_list'),
    path('rent-create/', RentCreateView.as_view(), name='rent_create'),
    path('rent-update/<int:pk>/', RentUpdateView.as_view(), name='rent_update'),
    path('rent-delete/<int:pk>/', RentDeleteView.as_view(), name='rent_delete'),
]