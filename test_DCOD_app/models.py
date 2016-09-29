from django.db import models


class Region(models.Model):
    role = models.CharField(max_length=20)
