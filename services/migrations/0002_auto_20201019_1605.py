# Generated by Django 3.1.1 on 2020-10-19 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Servicio',
        ),
        migrations.AlterModelOptions(
            name='servicio',
            options={'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]