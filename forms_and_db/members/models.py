from django.db import models

class Member(models.Model):
  objects = None
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

  def __str__(self):
    return f'{self.lastname}, {self.firstname}'