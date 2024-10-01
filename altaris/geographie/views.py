from django.shortcuts import render
from django.http import HttpResponse
from geographie.models import Province

# Create your views here.
def province_list(request):
    provinces = Province.objects.all()
    return render(
        request,
        "geographie/provinces.html",
        {'provinces' : provinces}
    )

def province_details(request, nom_province):
    province = Province.objects.get(nom=nom_province)
    dioceses = province.dioceses.all()
    return render(
        request,
        "geographie/province_details.html",
        {
            'province' : province,
            'dioceses' : dioceses
        }
    )
