from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Mascota
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

# Un ViewSet es una clase que proporciona una implementación de alto nivel para crear vistas relacionadas con un modelo
# por que crear una vista con ViewSet y no con APIview: por que asi facilita la creacion de la api completa por que DRF genera automaticamente los metodos CRUD #


# Create your views here.

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all() # define los objetos que el ViewSet va a manejar
    serializer_class = MascotaSerializers # define que serializador usaras para convertir los datos

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all() 
    serializer_class = ClienteSerializers

class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all() 
    serializer_class = VeterinarioSerializers

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all() 
    serializer_class = ConsultaSerializers

class  DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = Diagnostico.objects.all() 
    serializer_class = DiagnosticoSerializers
    

class MascotaPorNombre(APIView):
    def get(self, request):
        nombre = request.GET.get("Nombre", "").strip()

        if nombre:  
            mascotas = Mascota.objects.filter(Nombre__icontains=nombre) 

            if mascotas.exists(): 
                serializer = MascotaSerializers(mascotas, many=True)  
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response({"error": "No se encontró ninguna mascota con ese nombre"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"error": "Debes enviar un parámetro"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def Mascota_list(request):
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializers(mascotas, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MascotaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Mascota_detail(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)  

    if request.method == 'GET':
        serializer = MascotaSerializers(mascota)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = MascotaSerializers(mascota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mascota.delete()
        return Response({"message": "Mascota eliminada"}, status=status.HTTP_204_NO_CONTENT)