# mi modelo de drones

from django.db import models

class Drone(models.Model):
    nombre = models.CharField(max_lenggth=200, null=False, blank=False)
    año = models.CharField(max_length=200 null=False, blank=False)
    autonomia = models.CharField(max_length=200, null=False, blank=False)
    num_motores = models.CharField(max_length=2, null=False, blank=False)
    costo = models.CharField(max_length=6, null=False, blank=False)
