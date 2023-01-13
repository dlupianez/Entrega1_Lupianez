from django.views.generic import ListView, CreateView
#from django.shortcuts import render

from rentals.models import Rent
#from apartments.forms import ApartmentForm

class RentalsListView(ListView):
    model = Rent
    template_name = 'rentals/rentals-list.html'

class RentCreateView(CreateView):
    model = Rent
    template_name = 'rentals/rent-create.html'
    fields = '__all__'
    success_url = '/rentals/rentals-list/'