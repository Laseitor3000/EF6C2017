# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)


    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del candidato', max_length=128)


    """
   el id era para poder relacionar los votos con los candidatos y el nombre para identificarlo al candidato.
    """
    def __str__(self):
		return self.nombre


class Votos(models.Model):
    id = models.AutoField(primary_key=True) 
    #votos = models.SelectField('voto a candidato ', Candidatos)
    voto = models.ForeignKey(Candidato, blank=True, on_delete =models.CASCADE)
    
    
    """
el id era para poder llamar a los votos cuando hiciera las views pero no me salio y el voto es para saber los votos y a que candidato se voto. 
    """
    def __str__(self):
		return self.voto
    