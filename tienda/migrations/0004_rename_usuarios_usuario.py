# Generated by Django 4.2.3 on 2023-10-02 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_usuarios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]