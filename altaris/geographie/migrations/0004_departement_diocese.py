# Generated by Django 5.1.1 on 2024-09-30 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geographie', '0003_departement'),
    ]

    operations = [
        migrations.AddField(
            model_name='departement',
            name='diocese',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='departements', to='geographie.diocese'),
            preserve_default=False,
        ),
    ]
