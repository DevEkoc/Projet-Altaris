"""
URL configuration for altaris project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from geographie import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('provinces/', views.provinces_list, name="provinces-list"),
    path('provinces/<slug:slug>/dioceses', views.province_details, name="province-details"),
    path('provinces/<slug:province_slug>/<slug:diocese_slug>/zones', views.diocese_details, name="diocese-details"),
    path('provinces/<slug:province_slug>/<slug:diocese_slug>/zones/<slug:zone_slug>', views.zone_details, name="zone-details"),


    path('provinces/add/', views.province_add, name="province-add"),
    path('provinces/<slug:province_slug>/dioceses/add/', views.diocese_add, name="diocese-add"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)