from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.db import IntegrityError, transaction

from django.db.models import Q

from django.contrib import messages

from .models import *

# Create your views here.

def contratar(request,id):
    logueo = request.session.get("logueo", False)
    usuario = Usuario.objects.get(pk=logueo["id"])
    servicio = Servicio.objects.get(pk=id)
    
    try:
            

            mensaje = f"""
                <h1 style='color:pink;'> ℕ𝕒𝕟𝕟𝕪'𝕤 </h1>
                <h5 style='color:blue'>{usuario.nombre} {usuario.apellido}</h5>    
                <p>esta interesado en tus servicios.</p>
                <p>Correo: {usuario.correo}</p>
                <p>Servicio de interes: {servicio.nombre}</p>
                <p>Contactate con el acudiente para más información</p>
                <p>Nanny's ADSO, 2024</p>
                <h1>  </h1>
            """

            try:
                msg = EmailMessage("Nanny's ADSO", mensaje, settings.EMAIL_HOST_USER, [servicio.propietario])
                msg.content_subtype = "html"  # Habilitar html
                msg.send()
                messages.success(request, "Se ha enviado el correo al cuidador.")

            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            except Exception as e:
                return HttpResponse(f"Error: {e}")

    except Exception as e:
            print(f"{e}")

    
    return render(request, "tienda/index.html")

     
def login(request):
    if request.method == "POST":
        usuario = request.POST.get("nick")
        clave = request.POST.get("password")

        try:
            q = Usuario.objects.get(nick=usuario, password=clave)
            messages.success(request, "Bienvenido!!")
            # Guardar nombre del rol  y no su número
            datos = {
                "rol": q.rol,
                "nombre_rol": q.get_rol_display(),
                "nombre": f"{q.nombre} {q.apellido}",
				"foto": q.foto.url,
                "id": q.id

            }
            request.session["logueo"] = datos

            return render(request, "tienda/index.html")

        except Usuario.DoesNotExist:
            messages.error(request, "Usuario o contraseña no válidos..")

            return render(request, "tienda/registro/login.html")
    else:

        if request.session.get("logueo", False):
            return render(request, "tienda/index.html")
        else:
            return render(request, "tienda/registro/login.html")
        


def logout(request):
    try:
        del request.session["logueo"]
        messages.success(request, "Sesión cerrada correctamente!")
    except Exception as e:
        messages.error(request, f"Error: {e} ")
    return HttpResponseRedirect(reverse("tienda:login"))


def home(request):
    return render(request,"tienda/index.html")


def signUp(request):
    return render(request, "tienda/registro/signUp.html")


def nosotros(request):
    return render(request, "tienda/registro/nosotros.html")

def perfil(request):
    usuario = request.session.get("logueo", False)
    q = Usuario.objects.get(pk = usuario["id"])
    contexto = {"data": q}
    return render(request, "tienda/usuarios/perfil.html", contexto)

def editar_perfil(request):
    usuario = request.session.get("logueo", False)
    q = Usuario.objects.get(pk = usuario["id"])
    contexto = {"data": q}
    return render(request, "tienda/usuarios/editarPerfil.html", contexto)



def editar_usuario(request):
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        nick = request.POST.get("nick")
        correo = request.POST.get("correo")
        password = request.POST.get("password")
        rol = request.POST.get("rol")
        descripcion = request.POST.get("descripcion")
        id = request.POST.get("id")
        Usuario.objects.filter(pk=id).update(id=id,nombre = nombre, apellido = apellido, nick = nick ,correo = correo, password = password, rol = rol, descripcion = descripcion )
        try:
            messages.success(request,'Usuario actualizado')
        except Exception as e:
            messages.error( request, f"Error: {e}")

        return redirect('tienda:perfil')





############Aqui comienza el modulo de Usuarios######################################


def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "tienda/crud/usuarios.html", {
        'usuarios': usuarios
    })

#Quiero recordar que en esta parte se agrego el nick y el rol, teniendo encuenta la migracion#
def guardar_usuario(request):
    nombre = request.POST.get("nombre")
    apellido = request.POST.get("apellido")
    nick = request.POST.get("nick")
    correo = request.POST.get("correo")
    rol = request.POST.get("rol")
    password = request.POST.get("password")
    
    descripcion = request.POST.get("descripcion")
    try: 
        p = Usuario(nombre = nombre, apellido = apellido, nick = nick  ,correo = correo, password = password, rol = rol ,descripcion = descripcion)
        p.save()
        messages.success(request, 'usuarios agregado')

    except Exception as e:
        messages.error(request, f'Error:{e}')
      

    return redirect('tienda:login')

def eliminar_usuario(request, id):
    usuario = Usuario.objects.filter(pk=id)
    try:
        usuario.delete()
        messages.success(request,'Usuario eliminado')
    except Exception as e :
        messages.error(request, f"Error: {e}")

    return redirect('tienda:usuarios')

def detalle_usuario(request, id):
    usuario = Usuario.objects.get(pk=id)
    return render(request, "tienda/crud/usuarioEditar.html",{
        'usuarios' : usuario
    })



############Aqui comienza el modulo de servicios ######################################


def servicios(request):
    return render(request, "tienda/crud/servicio.html", {
        'servicios': servicios,
    })

def childCare(request):
    servicios_nino = Servicio.objects.filter(tipo="1")
    return render(request, "tienda/servicios/childCare.html", {
        'servicios': servicios_nino
    })


def seniorCare(request):
    servicios_adulto = Servicio.objects.filter(tipo="2")
    return render(request, "tienda/servicios/seniorCare.html", {
        'servicios': servicios_adulto
    })

def specialCare(request):
    servicios_especial = Servicio.objects.filter(tipo="3")
    return render(request, "tienda/servicios/specialCare.html", {
        'servicios': servicios_especial
    })

def allCare(request):
    allCare = Servicio.objects.all
    return render(request, "tienda/servicios/specialCare.html", {
        'servicios': allCare
    })


def nannyServicio(request):
    allCare = Servicio.objects.all()  
    return render(request, "tienda/servicios/nannyServicio.html", {
        'servicios': allCare,
    })



def guardar_servicio(request):
    try:
        propietario = request.POST.get("propietario")
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        descripcion = request.POST.get("descripcion")
        tipo = request.POST.get("tipo")
        
        try: 
            p = Servicio(nombre = nombre, precio = precio, descripcion = descripcion , tipo = tipo, propietario = propietario)
            p.save()
            messages.success(request, f'Servicio agregado')

        except Exception as e:
            messages.error(request, f'Error:{e}')
        
        return redirect('tienda:servicios')

    except Exception as e :
        messages.error(request, f"Error: {e}")

    return redirect('tienda:nannyServicio')


def eliminar_servicio(request, id):
    servicio = Servicio.objects.filter(pk=id)
    try:
        servicio.delete()
        messages.success(request,'Servicio eliminado')
    except Exception as e :
        messages.error(request, f"Error: {e}")

    return redirect('tienda:servicios')


def detalle_servicio(request, id):
    servicio = Servicio.objects.get(pk=id)
    return render(request, "tienda/crud/servicioEditar.html",{
        'servicios' : servicio
    })

def editar_servicio(request):
    nombre = request.POST.get("nombre")
    precio = request.POST.get("precio")
    descripcion = request.POST.get("descripcion")
    id = request.POST.get("id")
    Servicio.objects.filter(pk=id).update(id=id, nombre = nombre, precio = precio, descripcion = descripcion )
    try:
        messages.success(request,'Servicio actualizado')
    except Exception as e:
        messages.error( request, f"Error: {e}")

    return redirect('tienda:servicios')

    

#pagos


def pagos(request):

    pagos = Pago.objects.all()
    return render(request, "tienda/crud/pagos.html", {
        'pagos': pagos
    })

def guardar_pagos(request):
    monto = request.POST.get("monto")
    fecha_pago = request.POST.get("fecha_pago")
    metodo_pago = request.POST.get("metodo_pago")
    descripcion = request.POST.get("descripcion")
    try: 
        p = Pago(monto = monto, fecha_pago = fecha_pago, metodo_pago = metodo_pago, descripcion = descripcion)
        p.save()
        messages.success(request, 'Pago agregado')

    except Exception as e:
        messages.error(request, f'Error:{e}')
      
      
    return redirect('tienda:pagos')

def eliminar_pagos(request, id):
    pago = Pago.objects.filter(pk=id)
    try:
        pago.delete()
        messages.success(request,'Niño/Abuelo eliminado')
    except Exception as e :
        messages.error(request, f"Error: {e}")

    return redirect('tienda:pagos')

def detalle_pagos(request, id):
    pago = Pago.objects.get(pk=id)
    return render(request, "tienda/crud/pagoEditar.html",{
        'pagos' : pago
    })

def editar_pagos(request):
        monto = request.POST.get("monto")
        fecha_pago = request.POST.get("fecha_pago")
        metodo_pago = request.POST.get("metodo_pago")
        descripcion = request.POST.get("descripcion")
        id = request.POST.get("id")
        Pago.objects.filter(pk=id).update(id=id, monto = monto, fecha_pago = fecha_pago, metodo_pago = metodo_pago,  descripcion = descripcion )
        try:
            messages.success(request,'Pago actualizado')
        except Exception as e:
            messages.error( request, f"Error: {e}")

        return redirect('tienda:pagos')
    
    
    
    
#Padres



def padres(request):

    padres = Padre.objects.all()
    return render(request, "tienda/crud/padres.html", {
        'padres': padres
    })

def guardar_padres(request):
    nombre = request.POST.get("nombre")
    genero = request.POST.get("genero")
    fecha_nacimiento = request.POST.get("fecha_nacimiento")
    email = request.POST.get("email")
    telefono = request.POST.get("telefono")
    direccion = request.POST.get("direccion")
    descripcion = request.POST.get("descripcion")
    try: 
        p = Padre(nombre = nombre, genero = genero, fecha_nacimiento = fecha_nacimiento, email = email, telefono = telefono, direccion = direccion, descripcion = descripcion)
        p.save()
        messages.success(request, 'Padre agregado')

    except Exception as e:
        messages.error(request, f'Error:{e}')
      
      
    return redirect('tienda:padres')

def eliminar_padres(request, id):
    padre = Padre.objects.filter(pk=id)
    try:
        padre.delete()
        messages.success(request,'Padre eliminado')
    except Exception as e :
        messages.error(request, f"Error: {e}")

    return redirect('tienda:padres')

def detalle_padres(request, id):
    padre = Padre.objects.get(pk=id)
    return render(request, "tienda/crud/padreEditar.html",{
        'padres' : padre
    })

def editar_padres(request):
        nombre = request.POST.get("nombre")
        genero = request.POST.get("genero")
        fecha_nacimiento = request.POST.get("fecha_nacimiento")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        direccion = request.POST.get("direccion")
        descripcion = request.POST.get("descripcion")
        id = request.POST.get("id")
        Padre.objects.filter(pk=id).update(id=id,nombre = nombre, genero = genero, fecha_nacimiento = fecha_nacimiento, email = email, telefono = telefono, direccion = direccion, descripcion = descripcion )
        try:
            messages.success(request,'Padre actualizado')
        except Exception as e:
            messages.error( request, f"Error: {e}")

        return redirect('tienda:padres')




#ninoabuelos



def ninoabuelos(request):

    ninoabuelos = Ninoabuelo.objects.all()
    return render(request, "tienda/crud/ninoabuelos.html", {
        'ninoabuelos': ninoabuelos
    })

def guardar_ninoabuelos(request):
    nombre = request.POST.get("nombre")
    fecha_nacimiento = request.POST.get("fecha_nacimiento")
    numero_identificacion = request.POST.get("numero_identificacion")
    descripcion = request.POST.get("descripcion")
    try: 
        p = Ninoabuelo(nombre = nombre, fecha_nacimiento = fecha_nacimiento, numero_identificacion = numero_identificacion,  descripcion = descripcion)
        p.save()
        messages.success(request, 'Niño/Abuelo agregado')

    except Exception as e:
        messages.error(request, f'Error:{e}')

    return redirect('tienda:ninoabuelos')

def eliminar_ninoabuelos(request, id):
    ninoabuelo = Ninoabuelo.objects.filter(pk=id)
    try:
        ninoabuelo.delete()
        messages.success(request,'Niño/Abuelo eliminado')
    except Exception as e :
        messages.error(request, f"Error: {e}")

    return redirect('tienda:ninoabuelos')

def detalle_ninoabuelos(request, id):
    ninoabuelo = Ninoabuelo.objects.get(pk=id)
    return render(request, "tienda/crud/ninoabueloEditar.html",{
        'ninoabuelos' : ninoabuelo
    })

def editar_ninoabuelos(request):
        nombre = request.POST.get("nombre")
        fecha_nacimiento = request.POST.get("fecha_nacimiento")
        numero_identificacion = request.POST.get("numero_identificacion")
        descripcion = request.POST.get("descripcion")
        id = request.POST.get("id")
        Ninoabuelo.objects.filter(pk=id).update(id=id,nombre = nombre, fecha_nacimiento = fecha_nacimiento, numero_identificacion = numero_identificacion,  descripcion = descripcion )
        try:
            messages.success(request,'Niños/Abuelo actualizado')
        except Exception as e:
            messages.error( request, f"Error: {e}")

        return redirect('tienda:ninoabuelos')