# Generated by Django 5.0.2 on 2024-03-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_servicio_delete_producto_remove_padre_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'MenorEdad'), (2, 'TerceraEdad'), (3, 'CuidadoEspecial')], default=1),
        ),
    ]
