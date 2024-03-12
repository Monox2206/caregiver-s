# Generated by Django 5.0.2 on 2024-02-28 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_auto_20240226_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.FloatField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.RemoveField(
            model_name='padre',
            name='genero',
        ),
    ]
