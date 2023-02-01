"""real_estate_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from real_estate_management.views import about_me, elements_list, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rentals/', include('rentals.urls')),
    path('apartments/', include('apartments.urls')),
    path('tenants/', include('tenants.urls')),
    path('about-me/', about_me),
    path('elements-list/', elements_list),
    path('users/', include('users.urls')),
    path('', index, name='index'),    
]
