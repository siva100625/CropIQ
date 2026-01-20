from django.db import models

class soil(models.Model):
    moisture=models.FloatField(default=0)
    temperature=models.FloatField(default=0)

class Soildata(models.Model):
    district = models.CharField(max_length=100)
    ph = models.FloatField()
    texture = models.CharField(max_length=50)



    
