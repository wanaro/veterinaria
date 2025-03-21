from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


router = DefaultRouter()
router.register(r'Mascotas', MascotaViewSet) 
router.register(r'Clientes', ClienteViewSet) 
router.register(r'Veterinarios', VeterinarioViewSet)
router.register(r'Consultas', ConsultaViewSet)
router.register(r'Diagnosticos', DiagnosticoViewSet) 

urlpatterns = [
    path('api/', include(router.urls)), 
    path('Mascota/buscar/', MascotaPorNombre.as_view(), name='buscar-Nombre'),
    path('Mascotas/', Mascota_list, name='Mascota_list'),
    path('Mascotas/<int:pk>', Mascota_detail, name='Mascota_detail'),
]


# GET/api/Mascotas para listar las mascotas
# POST/api/Mascotas para crear una mascota
# GET/api/Mascotas/{id}/ para obtener una mascota en especifico
# Put/api/Mascotas/{id}/ para actualizar una mascota especifica
# DELETE/api/Mascotas/{id}/ para eliminar una mascota especifica #