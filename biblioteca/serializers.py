from rest_framework import serializers
from .models import Libro, Estudiante, Reserva

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'fecha_publicacion', 'isbn']


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'curso', 'codigo']


class ReservaSerializer(serializers.ModelSerializer):
    estudiante = EstudianteSerializer()
    libro = LibroSerializer()

    class Meta:
        model = Reserva
        fields = ['id', 'estudiante', 'libro', 'fecha_reserva']
