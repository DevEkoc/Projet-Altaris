# Generated by Django 5.1.1 on 2024-09-30 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geographie', '0005_diocese_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diocese',
            name='photo',
            field=models.ImageField(blank=True, default='photos/dioceses/default.jpeg', null=True, upload_to='photos/dioceses/'),
        ),
    ]
