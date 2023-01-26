from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def about_me(request):
    context = {
        'greet':'Hi people!',
        'name':'David Lupiañez',
        'age':39,
        'excerpt':'Bachelor degree in information systems, with extensive experience in various areas of software development. Strongly achievement-oriented and with outstanding teamwork skills. I have developed in numerous technologies and languages, currently I am specializing in Python and Django Framework.',
        'project':'Project is about apartment rentals, so applications need to be able to handle apartments, tenants and rental objects, and their relationships.',
        'country':'Argentina',
        'location':'Mendoza',
        'picture':"{% static 'images/profile2.jpg' %}",
    }
    return render(request, 'about/about-me.html', context=context)

