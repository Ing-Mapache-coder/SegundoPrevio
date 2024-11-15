from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.CharField(max_length=50)
    codigo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo


class Reserva(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva de {self.estudiante} para el libro {self.libro}"
