from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, EstudianteViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'reservas', ReservaViewSet, basename='reserva')

urlpatterns = [
    path('', include(router.urls)),
]
