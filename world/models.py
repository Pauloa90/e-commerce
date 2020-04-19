from django.db import models
class Lugares(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    imagens = models.ImageField(upload_to='imagens')

    def __str__(self):
        return self.name

