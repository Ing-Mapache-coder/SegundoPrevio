from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    completado = models.BooleanField(default=False)
    fecha_vencimiento = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="tareas")

    def __str__(self):
        return self.nombre
