from django.db import models

# Create your models here.
class Dicionario(models.Model):
    palavra = models.CharField(max_length=50, null=False, blank=False)
    pronuncia = models.CharField(max_length=50, null=True, blank=True)
    rima = models.CharField(max_length=20, null=True, blank=True)
    silabas = models.IntegerField()

    def __str__(self):
        return self.palavra