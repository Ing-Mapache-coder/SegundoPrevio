from rest_framework import serializers
from .models import Tarea, Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'correo']

class TareaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    
    class Meta:
        model = Tarea
        fields = ['id', 'nombre', 'descripcion', 'completado', 'fecha_vencimiento', 'usuario']
