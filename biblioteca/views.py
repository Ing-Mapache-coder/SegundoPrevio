from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Libro, Estudiante, Reserva
from .serializers import LibroSerializer, EstudianteSerializer, ReservaSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class ReservaViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def reservar_libro(self, request):
        estudiante_id = request.data.get('estudiante_id')
        libro_id = request.data.get('libro_id')

        estudiante = Estudiante.objects.get(id=estudiante_id)
        libro = Libro.objects.get(id=libro_id)

        reserva = Reserva.objects.create(estudiante=estudiante, libro=libro)
        return Response({'mensaje': f'Libro "{libro.titulo}" reservado por {estudiante.nombre}'})
