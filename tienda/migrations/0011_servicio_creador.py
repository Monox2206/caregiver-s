# Generated by Django 5.0.2 on 2024-03-02 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_servicio_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='creador',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
    ]
