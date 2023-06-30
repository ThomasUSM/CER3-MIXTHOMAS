from django.db import models

class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
