from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from apartments.models import Apartment


class ApartmentsListView(ListView):
    model = Apartment
    template_name = 'apartments/apartments-list.html'
    

class ApartmentCreateView(CreateView):
    model = Apartment    
    template_name = 'apartments/apartment-create.html'
    fields = ['door_number', 'rental_value', 'garage_value', 'expenses_value', 'is_available', 'apartment_picture']
    success_url = '/apartments/apartments-list/'

def list_apartments_search(request):
    print(request.GET['search'])
    if 'search' in request.GET:
        search = request.GET['search']
        apartments = Apartment.objects.filter(door_number__icontains=search)                
    else:
        apartments = Apartment.objects.all()
    context = {
        'apartments':apartments,
    }
    print(context)    
    return render(request, 'apartments/apartments-list-search.html', context=context)

class ApartmentUpdateView(UpdateView):
    model = Apartment
    template_name = 'apartments/apartment-update.html'
    fields = ['door_number', 'rental_value', 'garage_value', 'expenses_value', 'is_available', 'apartment_picture']
    success_url = '/apartments/apartments-list/'

class ApartmentDeleteView(DeleteView):
    model = Apartment
    template_name = 'apartments/apartment-delete.html'
    fields = '__all__'
    success_url = '/apartments/apartments-list/'