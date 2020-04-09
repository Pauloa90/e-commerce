from django.db import models

# Create your models here.
class Lugares(models.Model):
    continente = models.CharField(max_length=254, default='')
    imagens = models.ImageField(upload_to='images')

    def __str__(self):
        return self.continente