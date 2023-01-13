from django.views.generic import ListView, CreateView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apartments.models import Apartment

class ApartmentsListView(ListView):
    model = Apartment
    template_name = 'apartments/apartments-list.html'
    

class ApartmentCreateView(CreateView):
    model = Apartment
    template_name = 'apartments/apartment-create.html'
    fields = '__all__'
    success_url = '/apartments/apartments-list/'

def list_apartments_search(request):
    #print(request.method)
    if 'search' in request.GET:
        search = request.GET['search']
        apartments = Apartment.objects.filter(door_number__icontains=search)        
    else:
        apartments = Apartment.objects.all()
    context = {
        'apartments':apartments,
    }
    #print(context)    
    return render(request, 'apartments/apartments-list.html', context=context)

