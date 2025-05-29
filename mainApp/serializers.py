from rest_framework import serializers
from .models import Eventos, Funcion, Ubicacion, Ventas



class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'

class FuncionSerializer(serializers.ModelSerializer):
    evento = EventosSerializer(read_only=True)

    class Meta:
        model = Funcion
        fields = '__all__'

class UbicacionSerializer(serializers.ModelSerializer):
    disponibles = serializers.SerializerMethodField()

    class Meta:
        model = Ubicacion
        fields = ['id', 'nombre', 'precio', 'asientos_disponibles', 'asientos_vendidos', 'disponibles', 'funcion']

    def get_disponibles(self, obj):
        return obj.asientos_disponibles - obj.asientos_vendidos

class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = '__all__'
