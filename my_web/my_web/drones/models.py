from django.db import models
class Dron(models.Model):
    modelo = models.CharField(max_length=400, null=False, blank=False)
    año = models.CharField(max_length=400, null=False, blank=False, default="")

    def __str__(self):
        return "{} {}".format(self.modelo, self.año)

class camara(models.Model):
    modelo1 = models.CharField(max_length=400, null=False, blank=False)
    año1 = models.CharField(max_length=400, null=False, blank=False, default="")

    def __str__(self):
        return "{} {}".format(self.modelo1, self.año1)


   