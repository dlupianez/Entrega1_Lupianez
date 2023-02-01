from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from apartments.models import Apartment
from rentals.models import Rent
from tenants.models import Tenant
from real_estate_management.settings import MEDIA_ROOT

def about_me(request):
    context = {
        'greet':'Hi people!',
        'name':'David Lupiañez',
        'age':39,
        'excerpt':'Bachelor degree in information systems, with extensive experience in various areas of software development. Strongly achievement-oriented and with outstanding teamwork skills. I have developed in numerous technologies and languages, currently I am specializing in Python and Django Framework.',
        'project':'Project is about apartment rentals, so applications need to be able to handle apartments, tenants and rental objects, and their relationships.',
        'country':'Argentina',
        'location':'Mendoza',
        'picture': MEDIA_ROOT + 'profile2.jpg',
    }
    return render(request, 'about/about-me.html', context=context)

def elements_list(request):
    all_apartments = Apartment.objects.all()
    all_rents = Rent.objects.all()
    all_tenants = Tenant.objects.all()
    context = {
        'apartments':all_apartments,
        'rents':all_rents,
        'tenants':all_tenants,
    }
    return render(request, 'elements-list.html', context=context)

def index(request):
    return render(request, 'index.html', context={})