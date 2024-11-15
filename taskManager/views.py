from django.shortcuts import render
from rest_framework import viewsets
from .models import Tarea, Usuario
from .serializers import TareaSerializer, UsuarioSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('usuario', None)
        if user_id is not None:
            return self.queryset.filter(usuario_id=user_id)
        return self.queryset

    @action(detail=True, methods=['patch'])
    def marcar_como_realizada(self, request, pk=None):
        tarea = self.get_object()
        tarea.completado = True
        tarea.save()
        return Response({'status': 'tarea marcada como completada'}, status=status.HTTP_200_OK)
