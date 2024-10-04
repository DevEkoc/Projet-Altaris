# Generated by Django 5.1.1 on 2024-10-03 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geographie', '0014_delete_paroisse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paroisse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('localite', models.CharField(max_length=100)),
                ('initiales', models.CharField(help_text="Maxi 5 caractères. Les initiales de la localité. Ex : MBEN pour 'Mbenda'", max_length=5, unique=True)),
                ('saint_patron', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('personnelle', 'Personnelle'), ('territoriale', 'Territoriale')], default='territoriale', max_length=100)),
                ('statut', models.CharField(choices=[('paroisse', 'Paroisse'), ('basilique', 'Basilique'), ('cathedrale', 'Cathédrale'), ('sanctuaire', 'Sanctuaire'), ('paroisse-universitaire', 'Paroisse-universitaire'), ('quasi-paroisse', 'Quasi-Paroisse'), ('centre-eucharistique', 'Centre-Eucharistique')], default='paroisse', max_length=100)),
                ('localisation_gps', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('cure', models.CharField(max_length=100)),
                ('aumonier_paroissial', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, default='photos/default.jpeg', null=True, upload_to='photos/paroisse/')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paroisses', to='geographie.zone')),
            ],
        ),
    ]
