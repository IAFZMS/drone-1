# Generated by Django 2.2.7 on 2019-11-23 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0009_dron_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dron',
            old_name='tipo',
            new_name='Tipo_de_dron',
        ),
    ]
