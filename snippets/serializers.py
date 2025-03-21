from rest_framework import serializers
from .models import *

#  serializers.ModelSerializer) una clase del framework que facilita la creacion de los serializadores
# ventajas de usarlo automatizacion: que genera los campos del serializador con los campos del modelo
# facilita la creacion y validacion
# reduccion del codigo #

class MascotaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'
        read_only_fields = ['id']


class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ['id']

class VeterinarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = '__all__'
        read_only_fields = ['id']

class ConsultaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
        read_only_fields = ['id']

class DiagnosticoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = '__all__'
        read_only_fields = ['id']

# la clase meta es donde se define como se debe comportar el serializador con el modelo
# ejmplos:
# fields = ['id', 'nombre', 'categoria'] 
# para llamarlos a todos fields = '__all__'
# para excluir exclude = ['fecha_creacion']
# para que solo puedan ser leidos y no editados read_only_fields = ['id'] 
# para pasar configuraciones adicionales extra_kwargs = {'nombre': {'validators': []}} esto eliminaria los validadores para el campo#

