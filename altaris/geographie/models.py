from datetime import datetime
from enum import unique
import uuid

from django.db import models
from django.utils.text import slugify
import os
# Create your models here.
class Province(models.Model):
    id_province = models.AutoField(primary_key=True)

    nom = models.CharField(
        max_length=100, 
        help_text="Nom de la Province Ecclésiastique",
        blank=True,
        unique=True
    )
    
    archeveque = models.CharField(
        max_length=100, 
        blank=True, 
        default="Inconnu",
        help_text="Nom de l'Archevêque Métropolitain de la Province Ecclésiatique"
    )
    
    description = models.TextField(
        help_text="Une courte description de cette Province Ecclésiatique"
    )

    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:  # Si le slug n'existe pas déjà, le générer
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.nom}"


class Diocese(models.Model):
    CHOIX_DE_TYPE = [
        ('suffragant', 'Suffragant'),
        ('archeveche', 'Archevêché')
    ]

    def rename_photo(instance, filename):
        # Extraire l'extension du fichier
        extension = filename.split('.')[-1]
        # Générer un UUID pour rendre chaque nom de fichier unique
        unique_id = uuid.uuid4()
        new_filename = f"{slugify(instance.nom)}_{unique_id}.{extension}"
        return os.path.join('diocese_photos/', new_filename)

    nom = models.CharField(max_length=100, unique=True)
    localisation_gps = models.CharField(max_length=100)
    adresse = models.TextField()
    aumonier_diocesain = models.CharField(max_length=100)
    eveque = models.CharField(max_length=100)
    eveque_emerite = models.CharField(max_length=100, blank=True, null=True)
    saint_patron = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    photo = models.ImageField(upload_to=rename_photo, blank=True, null=True, default='photos/default.jpeg')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='dioceses')
    type = models.CharField(
        max_length=100,
        choices= CHOIX_DE_TYPE,
        default = 'suffragant'
    )
    slug = models.SlugField(
        max_length=100,
        blank = True,
        unique=True
    )
    def delete_photo_file(self):
        """
        Supprimer physiquement l'ancienne photo du système de fichiers si elle existe.
        """
        if self.photo and os.path.isfile(self.photo.path):
            os.remove(self.photo.path)

    def delete_old_photo(self):
        """
        Supprimer l'ancienne photo si elle existe et qu'une nouvelle est uploadée.
        """
        if self.pk:  # S'assurer que l'instance existe déjà dans la base de données
            try:
                # Récupérer l'ancienne photo avant la mise à jour
                old_photo = Diocese.objects.get(pk=self.pk).photo
                # Vérifier si une nouvelle photo est uploadée
                if old_photo and old_photo != self.photo and os.path.isfile(old_photo.path):
                    os.remove(old_photo.path)  # Supprimer l'ancienne photo du système de fichiers
            except Diocese.DoesNotExist:
                pass

    def save(self, *args, **kwargs):
        """
        Gérer la suppression de l'ancienne photo si une nouvelle est uploadée ou si la photo est supprimée.
        """
        # Supprimer l'ancienne photo si une nouvelle est uploadée
        self.delete_old_photo()

        # Appelle la méthode de sauvegarde par défaut
        super().save(*args, **kwargs)

        # Si la photo a été effacée dans le formulaire, la supprimer du système de fichiers
        if not self.photo:  # Si la photo a été supprimée via le formulaire
            self.delete_photo_file()

    def delete(self, *args, **kwargs):
        """
        Supprimer la photo du système de fichiers lors de la suppression de l'instance.
        """
        self.delete_photo_file()  # Supprime la photo avant de supprimer l'instance
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nom


class Region(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.nom


class Departement(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='departements')
    diocese = models.ForeignKey(Diocese, on_delete=models.CASCADE, related_name="departements")

    def __str__(self) -> str:
        return self.nom


class Zone(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    localisation_gps = models.CharField(max_length=100)
    adresse = models.TextField()
    aumonier_zonal = models.CharField(max_length=100)
    vicaire_episcopal = models.CharField(max_length=100)
    saint_patron = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/zones/', blank=True, null=True, default='photos/default.jpeg')
    diocese = models.ForeignKey(Diocese, on_delete=models.CASCADE, related_name="zones")
    slug = models.SlugField(
        max_length=100,
        blank = True,
        unique = True
    )

    def save(self, *args, **kwargs):
        if not self.slug:  # Si le slug n'existe pas déjà, le générer
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nom


class Paroisse(models.Model):
    CHOIX_DE_TYPE = [
        ('personnelle', 'Personnelle'),
        ('territoriale', 'Territoriale'),
    ]
    CHOIX_DE_STATUT = [
        ('paroisse', 'Paroisse'),
        ('basilique', 'Basilique'),
        ('cathedrale', 'Cathédrale'),
        ('sanctuaire', 'Sanctuaire'),
        ('paroisse-universitaire', 'Paroisse-universitaire'),
        ('quasi-paroisse', 'Quasi-Paroisse'),
        ('centre-eucharistique', 'Centre-Eucharistique')
    ]

    nom = models.CharField(max_length=100)
    localite = models.CharField(max_length=100)
    initiales = models.CharField(
        max_length=5,
        unique=True,
        help_text="Maxi 5 caractères. Les initiales de la localité. Ex : MBEN pour 'Mbenda'"
    )
    saint_patron = models.CharField(max_length=100)
    type = models.CharField(
        max_length=100,
        choices=CHOIX_DE_TYPE,
        default='territoriale'
    )
    statut = models.CharField(
        max_length=100,
        choices=CHOIX_DE_STATUT,
        default='paroisse'
    )
    localisation_gps = models.CharField(max_length=100)
    adresse = models.TextField()
    cure = models.CharField(max_length=100)
    aumonier_paroissial = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/paroisse/', blank=True, null=True, default='photos/default.jpeg')
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="paroisses")
