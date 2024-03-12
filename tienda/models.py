from django.db import models

# Create your models here.

class Servicio(models.Model):
    tipos = (
		(1, 'MenorEdad'),
		(2, 'TerceraEdad'),
        (3, 'CuidadoEspecial'),
	)
    nombre = models.CharField(max_length=30)
    tipo = models.IntegerField(choices=tipos, default=1)
    precio = models.FloatField(max_length=30)
    descripcion = models.CharField(max_length=200)
    propietario = models.CharField(max_length=200)
    
class Usuario(models.Model):
    ROLES = (
		(1, 'Padre'),
		(2, 'Nanny'),
		(3, 'Ninos/Abuelos'),
        (4, 'Administrador')
	)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nick = models.CharField(max_length=50)
    foto = models.ImageField(null=True, blank=True, upload_to='fotos', default="fotos/default.png")
    correo= models.CharField(max_length=30)
    password= models.CharField(max_length=15)
    rol = models.IntegerField(choices=ROLES, default=1)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
	    return f"{self.nick}"
    
class Padre(models.Model):

    nombre = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(max_length=30)
    email= models.CharField(max_length=15)
    telefono= models.CharField(max_length=15)
    direccion= models.CharField(max_length=15)
    descripcion = models.CharField(max_length=200)

class Ninoabuelo(models.Model):

    nombre = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(max_length=30)
    numero_identificacion = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

class Pago(models.Model):

    monto = models.FloatField(max_length=30)
    fecha_pago = models.DateField(max_length=30)
    metodo_pago = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

class Cita(models.Model):
    reservacion = models.CharField(max_length=200)
    fecha = models.DateTimeField(max_length=30)
    tipoServicio = models.CharField(max_length=100)
