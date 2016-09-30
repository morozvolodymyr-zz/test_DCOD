from django.db import models


class Region(models.Model):
    region = models.CharField(max_length=20)


class City(models.Model):
    city = models.CharField(max_length=20)
    population = models.PositiveIntegerField(default=0)
    id_region = models.ForeignKey(to=Region, on_delete=models.CASCADE, related_name='id_region')