from django.urls import path
from rentals.views import RentalsListView, RentCreateView

urlpatterns = [
    path('rentals-list/', RentalsListView.as_view(), name='rentals_list'),
    path('rent-create/', RentCreateView.as_view(), name='rent_create'),
]