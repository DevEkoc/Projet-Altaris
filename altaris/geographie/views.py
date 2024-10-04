from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Province, Diocese, Zone
from .forms import ProvinceForm, DioceseForm, ZoneForm, ParoisseForm


# Create your views here.
def provinces_list(request):
    provinces = Province.objects.all()
    return render(
        request,
        "geographie/provinces.html",
        {'provinces' : provinces}
    )

def province_details(request, slug):
    province = Province.objects.get(slug=slug)
    dioceses = province.dioceses.all()
    return render(
        request,
        "geographie/province_details.html",
        {
            'province' : province,
            'dioceses' : dioceses
        }
    )

def diocese_details(request, province_slug, diocese_slug):
    diocese = Diocese.objects.get(slug=diocese_slug)
    province = diocese.province
    zones = diocese.zones.all()
    return render(
        request,
        "geographie/diocese_details.html",
        {
            'province' : province,
            'diocese' : diocese,
            'zones' : zones
        }
    )

def zone_details(request, province_slug, diocese_slug, zone_slug):
    zone = Zone.objects.get(slug=zone_slug)
    paroisses = zone.paroisses.all()
    diocese = zone.diocese
    province = diocese.province

    return render(
        request,
        "geographie/zone_details.html",
        {
            'province' : province,
            'diocese' : diocese,
            'zone' : zone,
            'paroisses' : paroisses
        }
    )


def province_add(request):
    if request.method == "POST":
        form = ProvinceForm(request.POST)
        if form.is_valid():
            province = form.save(commit=False)
            province.save()
            return redirect('province-details', slug=province.slug)
    else:
        form = ProvinceForm()
    return render(
        request,
        "geographie/province_add.html",
        {'form' : form}
    )


def diocese_add(request, province_slug):
    province = Province.objects.get(slug=province_slug)
    if request.method == "POST":
        form = DioceseForm(request.POST, request.FILES)
        if form.is_valid():
            diocese = form.save(commit=False)  # Crée l'instance du diocèse mais ne la sauvegarde pas encore
            diocese.province = province  # Associe la province courante
            diocese.save()  # Maintenant, sauvegarde l'instance avec la province assignée
            return redirect('diocese-details', province_slug=province.slug, diocese_slug=diocese.slug)
    else:
        form = DioceseForm()
    form.fields['province'].initial = province
    form.fields['province'].disabled = True
    return render(
        request,
        "geographie/diocese_add.html",
        {
            'form': form,
            'province': province
        }
    )