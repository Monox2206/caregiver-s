from django.contrib import admin
from django.urls import path
from tienda import views
from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name = "tienda"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home, name='inicio' ),

    path("login/", views.login, name="login"),

    path("logout/", views.logout, name="logout"),
    
    path("nosotros/", views.nosotros, name="nosotros"),

    path("perfil/", views.perfil, name="perfil"),
 
    path("editar_perfil/", views.editar_perfil, name="editar_perfil"),

    path('signUp/', views.signUp, name='signUp'),

    
 #usuarios
    
    path('usuarios/', views.usuarios, name='usuarios'),

    path('usuarios/guardar', views.guardar_usuario, name='guardar_usuario'),
    
    path('usuarios/editar', views.editar_usuario, name='editar_usuario'),

    path('usuarios/eliminar/<int:id> ', views.eliminar_usuario, name='eliminar_usuario'),

    path('usuarios/detalle/<int:id> ', views.detalle_usuario, name='detalle_usuario'),

 #servicios
 
    path('servicios/', views.servicios, name='servicios'),
    
    path('contratar/<int:id>', views.contratar, name='contratar'),

    path('childCare/', views.childCare, name='childCare'),

    path('seniorCare/', views.seniorCare, name='seniorCare'),

    path('specialCare/', views.specialCare, name='specialCare'),

    path('allCare/', views.allCare, name='allCare'),

    path('nannyServicio/', views.nannyServicio, name='nannyServicio'),

    path('servicios/guardar/', views.guardar_servicio , name='guardar_servicio'),
    
    path('servicios/editar', views.editar_servicio, name='editar_servicio'),

    path('servicios/eliminar/<int:id>', views.eliminar_servicio, name='eliminar_servicio'),

    path('servicios/detalle/<int:id>', views.detalle_servicio, name='detalle_servicio'),

# pagos

    
    path('pagos/', views.pagos, name='pagos'),

    path('pagos/guardar', views.guardar_pagos, name='guardar_pagos'),

    path('pagos/eliminar/<int:id> ', views.eliminar_pagos, name='eliminar_pagos'),

    path('pagos/detalle/<int:id> ', views.detalle_pagos, name='detalle_pagos'),

    path('pagos/editar', views.editar_pagos, name='editar_pagos'),

    path("login/", views.login, name="login"),

    path("logout/", views.logout, name="logout"),

    path("perfil/", views.perfil, name="perfil"),

    
    
#PADRES


    path('padres/', views.padres, name='padres'),

    path('padres/guardar', views.guardar_padres, name='guardar_padres'),

    path('padres/eliminar/<int:id> ', views.eliminar_padres, name='eliminar_padres'),

    path('padres/detalle/<int:id> ', views.detalle_padres, name='detalle_padres'),

    path('padres/editar', views.editar_padres, name='editar_padres'),
    
    
#ninoabuelos


    path('ninoabuelos/', views.ninoabuelos, name='ninoabuelos'),

    path('ninoabuelos/guardar', views.guardar_ninoabuelos, name='guardar_ninoabuelos'),

    path('ninoabuelos/eliminar/<int:id> ', views.eliminar_ninoabuelos, name='eliminar_ninoabuelos'),

    path('ninoabuelos/detalle/<int:id> ', views.detalle_ninoabuelos, name='detalle_ninoabuelos'),

    path('ninoabuelos/editar', views.editar_ninoabuelos, name='editar_ninoabuelos'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

