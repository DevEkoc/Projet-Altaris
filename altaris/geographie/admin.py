from django.contrib import admin
from geographie.models import Province, Diocese, Region, Departement, Zone, Paroisse
from django.forms import TextInput, Textarea
from django.db import models


# Register your models here.
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['nom', 'id_province', 'archeveque']
admin.site.register(Province, ProvinceAdmin)

class DioceseAdmin(admin.ModelAdmin):
    list_display = ['nom', 'id', 'adresse','province', 'type', 'photo']
admin.site.register(Diocese, DioceseAdmin)

class RegionAdmin(admin.ModelAdmin):
    list_display = ['nom', 'id']
admin.site.register(Region, RegionAdmin)

class DepartementAdmin(admin.ModelAdmin):
    list_display = ['nom', 'id', 'region', 'diocese']
admin.site.register(Departement, DepartementAdmin)

class ZoneAdmin(admin.ModelAdmin):
    list_display = ['nom', 'id', 'aumonier_zonal', 'diocese']
admin.site.register(Zone, ZoneAdmin)

class ParoisseAdmin(admin.ModelAdmin):
    list_display = ['nom', 'id', 'cure', 'aumonier_paroissial', 'zone']
admin.site.register(Paroisse, ParoisseAdmin)
