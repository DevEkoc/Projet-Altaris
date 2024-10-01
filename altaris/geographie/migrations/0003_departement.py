# Generated by Django 5.1.1 on 2024-09-30 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geographie', '0002_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departements', to='geographie.region')),
            ],
        ),
    ]
