from django import forms
from .models import Province, Diocese, Zone, Paroisse
from django.core.exceptions import ValidationError
import os

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

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')

        if photo:
            # Vérification des extensions autorisées
            valid_extensions = ['jpg', 'jpeg', 'png']
            extension = photo.name.split('.')[-1].lower()
            if extension not in valid_extensions:
                raise ValidationError('Seuls les fichiers JPG, JPEG et PNG sont autorisés.')

            print(f"Taille du fichier : {photo.size} octets")  # Debugging pour vérifier la taille

            # Limitation de la taille à 800 Ko
            max_size = 800 * 1024
            if photo.size > max_size:
                raise ValidationError("La taille maximale autorisée pour la photo est de 800 Ko.")

        return photo


    class Meta:
        model = Diocese
        fields = ['nom', 'localisation_gps', 'adresse', 'aumonier_diocesain', 'eveque', 'eveque_emerite', 'saint_patron', 'description', 'photo', 'type']
        labels = {
            'nom': 'Nom du Diocèse',
            'type' : 'Choisissez le type de diocèse',
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












