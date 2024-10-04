from django.core.management.base import BaseCommand
from django.utils.text import slugify
from geographie.models import Province, Diocese, Zone


class Command(BaseCommand):
    help = 'Met à jour les slugs pour les modèles Province, Diocese et Zone'

    def handle(self, *args, **kwargs):
        # Mise à jour des slugs pour Province
        for province in Province.objects.all():
            if not province.slug:
                province.slug = slugify(province.nom)
                province.save()
                self.stdout.write(self.style.SUCCESS(f'Slug créé pour la Province {province.nom}'))

        # Mise à jour des slugs pour Diocese
        for diocese in Diocese.objects.all():
            if not diocese.slug:
                diocese.slug = slugify(diocese.nom)
                diocese.save()
                self.stdout.write(self.style.SUCCESS(f'Slug créé pour le Diocese {diocese.nom}'))

        # Mise à jour des slugs pour Zone
        for zone in Zone.objects.all():
            if not zone.slug:
                zone.slug = slugify(zone.nom)
                zone.save()
                self.stdout.write(self.style.SUCCESS(f'Slug créé pour la Zone {zone.nom}'))

        self.stdout.write(self.style.SUCCESS('Tous les slugs ont été mis à jour !'))
