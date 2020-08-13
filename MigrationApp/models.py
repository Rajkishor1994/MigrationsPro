from django.db import models

class Country(models.Model):
    country_id = models.IntegerField()
    country_name = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

class Sector(models.Model):
    sector_id = models.IntegerField()
    name = models.CharField(max_length=64)