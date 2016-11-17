from django.db import models

# Create your models here.
class Codigo(models.Model):
    codigo = models.TextField()
    nombre = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __str__(self):
        return self.nombre