from django.db import models

class City(models.Model):
  objects = None
  name = models.CharField(max_length=255)
  location = models.CharField(max_length=3)
  population = models.IntegerField()


def __str__(self):
    return f'{self.name}, {self.location}, {self.population}'