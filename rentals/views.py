from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rentals.models import Rent


class RentalsListView(LoginRequiredMixin, ListView):
    model = Rent
    template_name = 'rentals/rentals-list.html'

class RentCreateView(LoginRequiredMixin, CreateView):
    model = Rent
    template_name = 'rentals/rent-create.html'
    fields = '__all__'
    success_url = '/rentals/rentals-list/'

class RentUpdateView(UpdateView):
    model = Rent
    template_name = 'rentals/rent-update.html'
    fields = '__all__'
    success_url = '/rentals/rentals-list/'