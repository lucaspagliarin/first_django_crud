from django.db import models

# Create your models here.

class Pessoa(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)