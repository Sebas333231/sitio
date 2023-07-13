from django.db import models

# Create your models here.

class VentasAptos(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.CharField(max_length=500)
    imagen_dos = models.CharField(max_length=500)
    imagen_tres = models.CharField(max_length=500)
    precio = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.nombre} {self.precio}'
    


class Visita(models.Model):
    nombre_cliente = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    casa = models.ForeignKey (VentasAptos, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Agenda {self.id}:{self.nombre_cliente} {self.telefono}'
    

class comentarios(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comentario = models.CharField(max_length=500)
    fecha = models.DateTimeField()

    def __str__(self) -> str:
        return f'Comentario {self.id}:{self.nombre}{self.email}{self.comentario}{self.fecha}'