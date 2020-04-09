from django.db import models
class Lugares(models.Model):
    continente = models.CharField(max_length=254, default='')
    imagens = models.ImageField(upload_to='imagens')

    def __str__(self):
        return self.continente

