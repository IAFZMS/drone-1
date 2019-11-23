from django.db import models
TIPO_CHOICES = [
    ('F', 'Ala Fija'),
    ('R', 'Ala Rotatoria')
]

CAMARA_CHOICES = [
    ('I', 'INCLUIDA'),
    ('NI', 'NO INCLUIDA')
]


class Dron(models.Model):
    Tipo_de_dron= models.CharField(max_length=400, null=False, blank=False,default="----",choices=TIPO_CHOICES)
    modelo = models.CharField(max_length=400, null=False, blank=False, default="")
    autonomia = models.CharField(max_length=400, null=False, blank=False, default="")
    distancia = models.CharField(max_length=400, null=False, blank=False, default="")
    costo = models.CharField(max_length=400, null=False, blank=False, default="")
    camara_dron=models.CharField(max_length=400, null=False, blank=False,default="",choices=CAMARA_CHOICES)

    def __str__(self):
        return "Modelo: {}".format(self.modelo, self.año, self.autonomia, self.distancia, self.costo)

class camara(models.Model):
    Sensor = models.CharField(max_length=400, null=False, blank=False)
    Calidad = models.CharField(max_length=400, null=False, blank=False, default="")
    Objetivo= models.CharField(max_length=400, null=False, blank=False, default="")
    Resolucion= models.CharField(max_length=400, null=False, blank=False, default="")
    Rango_ISO= models.CharField(max_length=400, null=False, blank=False, default="")
    Velocidad_obturacion= models.CharField(max_length=400, null=False, blank=False, default="")
    def __str__(self):
        return "Sensor:{} Calidad:{} Objetivo: {} Resolucion: {} Rango Iso:{} Velocidad de obturación:{}".format(self.Sensor, self.Calidad, self.Objetivo, self.Resolucion, self.Rango_ISO, self.Velocidad_obturacion)