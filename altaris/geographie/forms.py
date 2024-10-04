from django import forms
from .models import Province, Diocese, Zone, Paroisse

class ProvinceForm(forms.ModelForm):
    template_name = 'geographie/snippets/province_form_snippet.html'

    class Meta:
        model = Province
        fields = ['nom', 'archeveque', 'description']
        labels = {
            'nom': 'Nom de la Province',
            'archeveque': 'Nom de l’Archevêque',
            'description': 'Description',
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'archeveque': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class DioceseForm(forms.ModelForm):
    template_name = 'geographie/snippets/diocese_form_snippet.html'

    class Meta:
        model = Diocese
        fields = ['nom', 'localisation_gps', 'adresse', 'aumonier_diocesain', 'eveque', 'eveque_emerite', 'saint_patron', 'description', 'photo', 'province', 'type']
        labels = {
            'nom': 'Nom du Diocèse',
            'province': 'Province Ecclésiastique',
            'type' : 'Type de diocèse',
            'eveque' : 'Nom de l\'Evêque',
            'eveque_emerite' : 'Nom de l\'Evêque Emérite',
            'aumonier_diocesain' : 'Nom de l\'Aumônier Diocésain',
            'saint_patron' : 'Saint Patron du Diocèse',
            'description' : 'Description',
            'adresse' : 'Adresse',
            'localisation_gps' : 'Localisation GPS',
            'photo' : 'Photo',
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du diocèse'}),
            'province': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'eveque': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'évêque'}),
            'eveque_emerite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'évêque émérite', 'optional': True}),
            'aumonier_diocesain': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'aumônier'}),
            'saint_patron': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saint Patron', 'optional': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'localisation_gps': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coordonnées GPS'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            province = kwargs.pop('province', None)  # Récupère la province courante
            super().__init__(*args, **kwargs)
            if province:
                self.fields['province'].initial = province  # Pré-remplir avec la province
                self.fields['province'].disabled = True  # Désactiver le champ

class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ['nom', 'localisation_gps', 'adresse', 'aumonier_zonal', 'vicaire_episcopal', 'saint_patron', 'description', 'photo', 'diocese']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la zone'}),
            'diocese': forms.Select(attrs={'class': 'form-control'}),
            'vicaire_episcopal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du Vicaire Episcopal'}),
            'aumonier_zonal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'aumônier zonal'}),
            'saint_patron': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saint Patron', 'optional': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'localisation_gps': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coordonnées GPS'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ParoisseForm(forms.ModelForm):
    class Meta:
        model = Paroisse
        fields = ['nom', 'localite', 'initiales', 'saint_patron', 'type', 'statut', 'localisation_gps', 'adresse', 'cure', 'aumonier_paroissial', 'description', 'photo', 'zone']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la paroisse'}),
            'localite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Localité'}),
            'zone': forms.Select(attrs={'class': 'form-control'}),
            'initiales': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Initiales (max 5 caractères)'}),
            'saint_patron': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saint Patron'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'cure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du curé'}),
            'aumonier_paroissial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'aumônier paroissial'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'localisation_gps': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coordonnées GPS'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }